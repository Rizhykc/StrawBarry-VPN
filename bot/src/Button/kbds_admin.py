from aiogram.types import KeyboardButton as keybutt
from aiogram.utils.keyboard import ReplyKeyboardMarkup

kb = [
    [
        keybutt(text='Добавить подписку'),
        keybutt(text='Изменить подписку'),
    ],
    {
        keybutt(text='Удалить подписку'),
        keybutt(text='Я так, просто посмотреть зашел'),
    }
]

main_admin = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder='Что Вас интересует?'
)

