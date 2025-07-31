from aiogram.types import InlineKeyboardButton as In
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

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
