from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton as keybutt
from aiogram.utils.keyboard import ReplyKeyboardMarkup

main_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            keybutt(text='Добавить подписку'),
            keybutt(text='Ассортимент'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что Вас интересует?'
)


inline_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Изменить', callback_data='update'),
     InlineKeyboardButton(text='Удалить', callback_data='delete')],
])
