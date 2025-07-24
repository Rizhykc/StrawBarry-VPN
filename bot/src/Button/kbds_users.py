from aiogram.types import InlineKeyboardButton as In
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.database.orm_query import get_all_keys

main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [In(text='Нажми сюда, чтобы узнать, что я умею',
        callback_data='help')],
])

help_inline = InlineKeyboardMarkup(inline_keyboard=[
    [In(text='Vpn', callback_data='vpn')],
    [In(text='Связь с админом бота', callback_data='admin')],
])

admin_inline = InlineKeyboardMarkup(inline_keyboard=[
    [In(text='Вернуться назад', callback_data='help')]
])

vpn_inline = InlineKeyboardMarkup(inline_keyboard=[
    [In(text='Выбрать сервер', callback_data='servers')],
    [In(text='Вернуться назад', callback_data='help')],
])


async def key():
    all_key = await get_all_keys()
    keyboard = InlineKeyboardBuilder()
    for key in all_key:
        keyboard.add(In(text=key.name,
                        callback_data=f'key_{key.id}'))
    keyboard.add(In(text='На главную', callback_data='vpn'))
