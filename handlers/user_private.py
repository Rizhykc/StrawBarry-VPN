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
    await callback.message.edit_text('С чем тебе помочь ?',
                                     reply_markup=kb.help_inline)

@user_router.callback_query(F.data == "vpn")
async def vpn_menu(callback: CallbackQuery):
    await callback.answer('Ты выбрал(а), vpn')
    await callback.message.edit_text('Что именно тебя интересует ?',
                                     reply_markup=kb.vpn_inline)

@user_router.callback_query(F.data == 'vpn_inst')
async def vpn_inst(callback: CallbackQuery):
    await callback.answer('Инструкция for you')
    await callback.message.edit_text('Инструкция!',
                                     reply_markup=kb.vpn_inst)

@user_router.callback_query(F.data == 'servers')
async def vpn_server(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('сервера!',
                                     reply_markup=kb.vpn_server)

@user_router.callback_query(F.data == "proxi")
async def proxi_menu(callback: CallbackQuery):
    await callback.answer('Ты выбрал(а), proxi')
    await callback.message.edit_text('Что именно тебя интересует ?',
                                     reply_markup=kb.proxi_inline)

@user_router.callback_query(F.data == "info")
async def proxi_info(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Информация о proxi',
                                     reply_markup=kb.proxi_info)
    
@user_router.callback_query(F.data == "prox_inst")
async def prox_inst(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Инструкция proxi',
                                     reply_markup=kb.proxi_inst)

@user_router.callback_query(F.data == "2ip")
async def you_ip(callback: CallbackQuery):
    await callback.answer('А я знаю, где ты находишься))')
    await callback.message.reply_location()
