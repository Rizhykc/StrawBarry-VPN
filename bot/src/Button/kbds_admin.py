from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Что хотите сделать хозяин ?',
                          callback_data='menu')],
])
