from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardMarkup, InlineKeyboardButton)


main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Нажми сюда, чтобы узнать, что я умею', callback_data='help')]
])

help_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Vpn', callback_data='vpn'),
     InlineKeyboardButton(text='Proxi', callback_data='proxi')],
    [InlineKeyboardButton(text='Узнать мое расположение', callback_data='2ip')]
])

vpn_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Инструкция по установке', callback_data='instuct')],
    [InlineKeyboardButton(text='Выбрать другой сервер', callback_data='servers')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='help')]
])



# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Нажми сюда, чтобы узнать, что я умею')]],
#     resize_keyboard=True, input_field_placeholder='Жмякай')

# help = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='vpn')],
#     [KeyboardButton(text='proxi')],
#     [KeyboardButton(text='Узнать мое расположение')]
# ], resize_keyboard=True, input_field_placeholder='Выбэри чо тэбэ нужьно')