from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from sqlalchemy.ext.asyncio import AsyncSession

from src.Button import kbds_admin as kb
from src.database.orm_query import orm_add_subscription, orm_get_subscriptions
from src.filters.chat_types import ChatTypeFilter, IsAdmin

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())


class AddProduct(StatesGroup):
    name = State()
    description = State()
    texts = {
        'AddProduct:name': 'Введите название заново:',
        'AddProduct:description': 'Введите описание заново:',
    }


@admin_router.message(Command('admin'))
async def admin_features(message: types.Message):
    await message.answer('Что хотите сделать?', reply_markup=kb.main_admin)


@admin_router.message(F.text == 'Ассортимент')
async def starring_at_product(message: types.Message, session: AsyncSession):
    await message.answer('ОК, вот список VPN')
    for product in await orm_get_subscriptions(session):
        await message.answer(text=f'\n{product.name}'
                             f'\n<pre>{product.description}</pre>')
    await message.answer('')


# FSM
@admin_router.message(StateFilter(None), F.text == 'Добавить подписку')
async def add_product(message: types.Message, state: FSMContext):
    await message.answer(
        'Введите название подписки', reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(AddProduct.name)


@admin_router.message(StateFilter('*'), Command('отмена'))
@admin_router.message(StateFilter('*'), F.text.casefold() == 'отмена')
async def cancel_handler(message: types.Message, state: FSMContext):

    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer('Действия отменены', reply_markup=kb.main_admin)


@admin_router.message(StateFilter('*'), Command('назад'))
@admin_router.message(StateFilter('*'), F.text.casefold() == 'назад')
async def back_step_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == AddProduct.name:
        await message.answer('Предидущего шага нет, или введите название '
                             'подписки или напишите "отмена"')
        return
    previous = None
    for step in AddProduct.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer('Ок, вы вернулись к прошлому шагу \n'
                                 f'{AddProduct.texts[previous.state]}')
            return
        previous = step


@admin_router.message(AddProduct.name, F.text)
async def add_name(message: types.Message, state: FSMContext):
    if len(message.text) >= 100:
        await message.answer('Название подписки не должно превышать 100 '
                             'символов.\n Введите заново')
        return
    await state.update_data(name=message.text)
    await message.answer('Введите описание подписки')
    await state.set_state(AddProduct.description)


@admin_router.message(AddProduct.name)
async def add_name2(message: types.Message, state: FSMContext):
    await message.answer('Вы ввели не допустимые данные, введите текст '
                         'названия подписки')


@admin_router.message(AddProduct.description, F.text)
async def add_key_vpn(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession
):
    await state.update_data(description=message.text)
    data = await state.get_data()
    try:
        await orm_add_subscription(session, data)
        await message.answer('Подписка добавлена', reply_markup=kb.main_admin)
        await state.clear()
    except Exception as e:
        await message.answer(
            f'Ошибка:\n{str(e)}\nБро опять что-то намудрил',
            reply_markup=kb.main_admin
        )
        await state.clear()


@admin_router.message(AddProduct.description)
async def add_description(message: types.Message, state: FSMContext):
    await message.answer('Вы ввели не допустимые данные, введите текст '
                         'описания подписки')
