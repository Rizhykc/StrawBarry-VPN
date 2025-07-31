import math

from bot.const import KEYS_PAGE


class Paginator:

    def __init__(self, array: list | tuple, page, per_page):
        self.array = array
        self.per_page = per_page
        self.page = page
        self.len = len(self.array)
        self.pages = math.ceil(self.len / self.per_page)

    def __get_slice(self):
        start = (self.page - KEYS_PAGE) * self.per_page
        stop = start + self.per_page
        return self.array[start:stop]

    def get_page(self):
        page_items = self.__get_slice()
        return page_items

    def has_next(self):
        if self.page < self.pages:
            return self.page + KEYS_PAGE
        return False

    def has_previous(self):
        if self.page > KEYS_PAGE:
            return self.page - KEYS_PAGE
        return False

    def get_next(self):
        if self.page < self.pages:
            self.page += KEYS_PAGE
            return self.get_page()
        raise IndexError('Next page does not exist. ',
                         'Use has_next() to check before.')

    def get_previous(self):
        if self.page > KEYS_PAGE:
            self.page -= KEYS_PAGE
            return self.__get_slice()
        raise IndexError('Previous page does not exist. ',
                         'Use has_previous() to check before.')

# from typing import List

# from aiogram import types
# from aiogram.types import CallbackQuery, InlineKeyboardButton as In
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.filters import Text
# from sqlalchemy.ext.asyncio import AsyncSession

# from admin_private import admin_router
# from bot.const import KEYS_PAGE
# from src.database.orm_query import get_all_keys


# def show_keys_page(
#     message: types.Message,
#     all_keys: List[types.Key],
#     page: int,
#     session: AsyncSession
# ):
#     """Показывает страницу с ключами."""
#     keyboard = InlineKeyboardBuilder()
#     total_pages = (len(all_keys) + KEYS_PAGE - 1) // KEYS_PAGE
#     start_idx = page * KEYS_PAGE
#     page_keys = all_keys[start_idx:start_idx + KEYS_PAGE]
#     if page < 0 or page >= total_pages:
#         raise ValueError('Неверный номер страницы')

#     keys_text = "\n".join(
#         f"{i+1}. {key.name} (ID: {key.id})"
#         for i, key in enumerate(page_keys, start=start_idx + 1)
#     )
    # await message.answer(text=f'🔑Список ключей (стр.
    #                      {page + 1}/{total_pages}):\n{keys_text}')
#     for key in page_keys:
#         keyboard.button(text=key.name, callback_data=f'key_{key.id}')

#     if total_pages > 1:
#         if page > 0:
#             keyboard.button(text='⬅️ Назад', callback_data=f'prev_{page}')
#         if page < total_pages - 1:
#             keyboard.button(text='Вперед ➡️', callback_data=f'next_{page}')

#     keyboard.button(text='На главную', callback_data='vpn')
#     keyboard.adjust(2, 1)
#     if total_pages > 1:
#         keyboard.adjust(2, len(page_keys))
#     keyboard.adjust(1, len(page_keys) + (2 if total_pages > 1 else 0))

#     text = f"Страница {page+1}/{total_pages}\n" if total_pages > 1 else ""
#     text += "Выберите ключ:" if page_keys else "Нет доступных ключей"


# @admin_router.callback_query(Text(startswith="page_"))
# async def handle_pagination(callback: CallbackQuery, session: AsyncSession):
#     page = int(callback.data.split("_")[1])
#     all_keys = await get_all_keys(session)
#     await show_keys_page(callback.message, all_keys, page)
#     await callback.answer()
