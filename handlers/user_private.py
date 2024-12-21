from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import Button.keyboard as kb

user_router = Router()

@user_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.reply(f'Привет! {message.from_user.first_name}\nЯ семейный помощник по вопросу VPN или Proxi',
                         reply_markup=kb.main_inline)

@user_router.callback_query(F.data == 'help')
async def help_menu(callback: CallbackQuery):
    await callback.answer('Сейчас, сейчас')
    await callback.message.edit_text('С чем тебе помочь ?', reply_markup=kb.help_inline)

@user_router.callback_query(F.data == "vpn")
async def vpn_menu(callback: CallbackQuery):
    await callback.answer('Ты выбрал(а), vpn')
    await callback.message.edit_text('Что именно тебя интересует ?', reply_markup=kb.vpn_inline)

@user_router.callback_query(F.data == "proxi")
async def proxi_menu(callback: CallbackQuery):
    await callback.answer('Ты выбрал(а), proxi')

@user_router.callback_query(F.data == "2ip")
async def you_ip(callback: CallbackQuery):
    await callback.answer('А я знаю, где ты находишься))')
    await callback.message.reply_location()
