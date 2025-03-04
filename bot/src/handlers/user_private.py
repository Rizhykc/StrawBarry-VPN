from aiogram import F, Router
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

import const as txt
from src.Button import kbds_users as kb
from src.database.orm_query import orm_get_subscriptions

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


@user_router.callback_query(F.data == "vpn")
async def vpn_menu(callback: CallbackQuery):
    await callback.answer('Ты выбрал(а), vpn')
    await callback.message.edit_text(text=txt.VPN_INST,
                                     reply_markup=kb.vpn_inline)


@user_router.callback_query(F.data == 'servers')
async def vpn_server(callback: CallbackQuery, session: AsyncSession):
    await callback.answer('Идет загрузка!')
    products = await orm_get_subscriptions(session)
    for product in products:
        await callback.message.answer(
            text=f'\n{product.name}\n<pre>{product.description}</pre>',
            reply_markup=kb.vpn_server
        )


@user_router.callback_query(F.data == "proxi")
async def proxi_menu(callback: CallbackQuery):
    await callback.answer('Ты выбрал(а), proxi')
    await callback.message.edit_text(text=txt.PROXI_INFO,
                                     reply_markup=kb.proxi_inline)


@user_router.callback_query(F.data == "prox_inst")
async def prox_inst(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text=txt.PROXI_INST,
                                     reply_markup=kb.proxi_inst)


@user_router.callback_query(F.data == "2ip")
async def you_ip(callback: CallbackQuery):
    await callback.answer('Пока не работает!')
