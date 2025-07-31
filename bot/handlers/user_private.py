import utils.const as txt
from aiogram import F, Router
from aiogram.types import CallbackQuery

from Button import kbds_users as kb

user_router = Router()


@user_router.callback_query(F.data == 'help')
async def help_menu(callback: CallbackQuery):
    await callback.answer('Сейчас, сейчас')
    await callback.message.edit_text('С чем тебе помочь ?',
                                     reply_markup=kb.help_inline)


@user_router.callback_query(F.data == 'admin')
async def admin_info(callback: CallbackQuery):
    await callback.answer(text=txt.ADMIN_TEXT,
                          show_alert=True)
    await callback.message.edit_text(text=txt.ADMIN_HELP,
                                     reply_markup=kb.admin_inline)


@user_router.callback_query(F.data == 'vpn')
async def vpn_menu(callback: CallbackQuery):
    await callback.answer('Ты выбрал(а), vpn')
    await callback.message.edit_text(text=txt.VPN_INST,
                                     reply_markup=kb.vpn_inline)


@user_router.callback_query(F.data == 'country')
async def vpn_country(callback: CallbackQuery):
    await callback.answer('Идет загрузка!')
    await callback.message.edit_text(text='Выберите страну',
                                     reply_markup=await kb.country())


@user_router.callback_query(F.data.startswith('country_'))
async def country(callback: CallbackQuery):
    await callback.answer('Вы выбрали страну')
    await callback.message.edit_text(text='<pre>item_data</pre>')
