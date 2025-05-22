from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from sqlalchemy.ext.asyncio import AsyncSession

from src.Button import kbds_admin as kb
from src.Button import kbds_users as kbs
from src.database.orm_query import orm_add_country
from src.filters.chat_types import ChatTypeFilter, IsAdmin

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())


class AddCountry(StatesGroup):
    name = State()
    texts = {
        'AddProduct:name': 'Введите название страны заново:',
    }


class AddKey(StatesGroup):
    name = State()
    key = State()
    country = State()
    texts = {
        'AddProduct:name': 'Введите ключ заново:',
        'AddProduct:key': 'Введите корректный ключ',
        'AddProduct:country': 'Выберете сущестувующую страну',
    }


@admin_router.message(Command('admin'))
async def admin_features(message: types.Message):
    await message.answer('Что хотите сделать?', reply_markup=kb.main_admin)


@admin_router.message(F.text == 'Ассортимент')
async def starring_at_product(message: types.Message, session: AsyncSession):
    await message.answer(text='ОК, вот список cтран',
                         reply_markup=await kbs.country())


# FSM
@admin_router.message(StateFilter(None),
                      F.text == 'Добавить cтрану',
                      Command('add_country'))
async def add_product(message: types.Message, state: FSMContext):
    await message.answer(
        'Введите название Страны', reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(AddCountry.name)


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
    if current_state == AddCountry.name:
        await message.answer('Предидущего шага нет, или введите название '
                             'страны или напишите "отмена"')
        return
    previous = None
    for step in AddCountry.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer('Ок, вы вернулись к прошлому шагу \n'
                                 f'{AddCountry.texts[previous.state]}')
            return
        previous = step


@admin_router.message(AddCountry.name, F.text)
async def add_name(message: types.Message,
                   state: FSMContext,
                   session: AsyncSession):
    if len(message.text) >= 100:
        await message.answer('Название подписки не должно превышать 100 '
                             'символов.\n Введите заново')
        return
    await state.update_data(name=message.text)
    data = await state.get_data()
    try:
        await orm_add_country(session, data)
        await message.answer('Страна добавлена', reply_markup=kb.main_admin)
        await state.clear()
    except Exception as e:
        await message.answer(
            f'Ошибка:\n{str(e)}\nБро опять что-то намудрил',
            reply_markup=kb.main_admin
        )
        await state.clear()


@admin_router.message(AddCountry.name)
async def add_name2(message: types.Message, state: FSMContext):
    await message.answer('Вы ввели не допустимые данные, '
                         'введите названия страны')



# @admin_router.message(AddCountry.description, F.text)
# async def add_key_vpn(
#     message: types.Message,
#     state: FSMContext,
#     session: AsyncSession
# ):
#     await state.update_data(description=message.text)
#     data = await state.get_data()
#     try:
#         await orm_add_subscription(session, data)
#         await message.answer('Подписка добавлена', reply_markup=kb.main_admin)
#         await state.clear()
#     except Exception as e:
#         await message.answer(
#             f'Ошибка:\n{str(e)}\nБро опять что-то намудрил',
#             reply_markup=kb.main_admin
#         )
#         await state.clear()


# @admin_router.message(AddCountry.description)
# async def add_description(message: types.Message, state: FSMContext):
#     await message.answer('Вы ввели не допустимые данные, введите текст '
#                          'описания подписки')
