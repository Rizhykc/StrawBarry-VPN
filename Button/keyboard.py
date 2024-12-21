from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Нажми сюда, чтобы узнать, что я умею', callback_data='help')],
])

help_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Vpn', callback_data='vpn'),
     InlineKeyboardButton(text='Proxi', callback_data='proxi')],
    [InlineKeyboardButton(text='Узнать мое расположение', callback_data='2ip')],
    [InlineKeyboardButton(text='Связь с админом бота', callback_data='admin')],
])

vpn_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Инструкция по установке', callback_data='vpn_inst')],
    [InlineKeyboardButton(text='Выбрать сервер', callback_data='servers')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='help')],
])

vpn_inst = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выбрать сервер', callback_data='servers')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='vpn')],
])
#  изменить !
vpn_server = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Здесь должны быть сервера', callback_data='vpn') ],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='vpn')],
])

proxi_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Что это и зачем ? Инфоблог о proxi', callback_data='info')],
    [InlineKeyboardButton(text='Инструкция по установке', callback_data='prox_inst')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='help')],
])

proxi_info = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Инструкция по установке', callback_data='prox_inst')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='proxi')],
])
#  изменить !п
proxi_inst = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='здесь должна быть инструкция', callback_data='proxi')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='proxi')],
])


# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Нажми сюда, чтобы узнать, что я умею')]],
#     resize_keyboard=True, input_field_placeholder='Жмякай')

# help = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='vpn')],
#     [KeyboardButton(text='proxi')],
#     [KeyboardButton(text='Узнать мое расположение')]
# ], resize_keyboard=True, input_field_placeholder='Выбэри чо тэбэ нужьно')