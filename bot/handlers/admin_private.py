from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton as In
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.ext.asyncio import AsyncSession

from Button import kbds_admin as kb
from Button import kbds_users as kbs
from filters.chat_types import ChatTypeFilter, IsAdmin

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())


class AddKey(StatesGroup):
    name = State()
    key = State()
    texts = {
        'AddProduct:name': 'Введите ключ заново:',
        'AddProduct:key': 'Введите корректный ключ',
    }


@admin_router.message(Command('admin'))
async def admin_features(message: types.Message):
    await message.answer('Что хотите сделать?', reply_markup=kb.main_admin)


@admin_router.message(F.text == 'Ассортимент')
async def starring_at_product(message: types.Message, session: AsyncSession):
    keyboard = InlineKeyboardBuilder()
    for key in await get_all_keys(session):
        keyboard.add(In(text=key.name,
                        callback_data=f'key_{key.id}'))
    keyboard.add(In(text='На главную', callback_data='vpn'))
    await message.answer(keyboard)


# FSM
@admin_router.message(StateFilter(None), F.text == 'Добавить ключ')
async def add_product(message: types.Message, state: FSMContext):
    await message.answer(
        'Введите название ключа', reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(AddKey.name)


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
    if current_state == AddKey.name:
        await message.answer('Предидущего шага нет, или введите название '
                             'ключа или напишите "отмена"')
        return
    previous = None
    for step in AddKey.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer('Ок, вы вернулись к прошлому шагу \n'
                                 f'{AddKey.texts[previous.state]}')
            return
        previous = step


@admin_router.message(AddKey.name, F.text)
async def add_name(message: types.Message, state: FSMContext):
    if len(message.text) >= 100:
        await message.answer('Название подписки не должно превышать 100 '
                             'символов.\n Введите заново')
        return
    await state.update_data(name=message.text)
    await message.answer('Введите ключ')
    await state.set_state(AddKey.key)


@admin_router.message(AddKey.name)
async def add_name_err(message: types.Message, state: FSMContext):
    await message.answer('Вы ввели не допустимые данные, '
                         'введите названия страны')


@admin_router.message(AddKey.key, F.text)
async def add_key(message: types.Message,
                  state: FSMContext,
                  session: AsyncSession):
    await state.update_data(key=message.text)
    data = await state.get_data()
    try:
        await orm_add_key(session, data)
        await message.answer('Ключ добавлен', reply_markup=kb.main_admin)
        await state.clear()
    except Exception as e:
        await message.answer(
            f'Ошибка:\n{str(e)}\nБро опять что-то намудрил',
            reply_markup=kb.main_admin
        )
        await state.clear()


@admin_router.message(AddKey.key)
async def add_key_err(message: types.Message, state: FSMContext):
    await message.answer('Вы ввели не допустимые данные, введите ключ')
