from aiogram.types import KeyboardButton as keybutt, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardMarkup


kb = [
    [
        keybutt(text='Добавить подписку'),
        keybutt(text='Ассортимент'),
    ]
]

main_admin = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder='Что Вас интересует?'
)


inline_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Изменить', callback_data='update'),
     InlineKeyboardButton(text='Удалить', callback_data='delete')],
])
