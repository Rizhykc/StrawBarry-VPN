from aiogram.types import InlineKeyboardButton as In
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.orm_query import orm_get_countries, orm_get_keys

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


async def country():
    all_country_name = await orm_get_countries()
    keyboard = InlineKeyboardBuilder()
    for country in all_country_name:
        keyboard.add(In(text=country.name,
                        callback_data=f'country_{country.id}'))
    keyboard.add(In(text='Вернуться назад', callback_data='vpn'))
    return keyboard.adjust(2).as_markup()


async def key():
    all_key = await orm_get_keys()
    keyboard = InlineKeyboardBuilder()
    for key in all_key:
        keyboard.add(In(text=key.name,
                        callback_data=f'key_{key.id}'))
    keyboard.add(In(text='На главную', callback_data='vpn'))

# задел на будущее !

# vpn_inst = InlineKeyboardMarkup(inline_keyboard=[
#     [In(text='android', callback_data='android'),
#      In(text='iOS', callback_data='ios')],
#     [In(text='Windows', callback_data='windows')],
#     [In(text='Вернуться назад', callback_data='vpn')],
# ])

# proxi_inline = InlineKeyboardMarkup(inline_keyboard=[
#     [In(text='Инструкция по установке', callback_data='prox_inst')],
#     [In(text='Вернуться назад', callback_data='help')],
# ])

# proxi_inst = InlineKeyboardMarkup(inline_keyboard=[
#     [In(text='Вернуться назад', callback_data='proxi')],
# ])


# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Нажми сюда, чтобы узнать, что я умею')]],
#     resize_keyboard=True, input_field_placeholder='Жмякай')

# help = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='vpn')],
#     [KeyboardButton(text='proxi')],
#     [KeyboardButton(text='Узнать мое расположение')]
# ], resize_keyboard=True, input_field_placeholder='Выбэри чо тэбэ нужьно')
