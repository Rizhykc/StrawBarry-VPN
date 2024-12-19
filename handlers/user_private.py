from aiogram import  F, types, Router
from aiogram.filters import CommandStart, Command, or_f

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет, я виртуальный помощник")

@user_private_router.message(or_f(Command("help"), (F.text.lower() == "Что ты умеешь?")))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню:")

@user_private_router.message(F.text.lower() == "VPN")
@user_private_router.message(Command("vpn"))
async def about_cmd(message: types.Message):
    await message.answer("О нас:")


@user_private_router.message(F.text.lower() == "Proxi")
@user_private_router.message(Command("proxi"))
async def payment_cmd(message: types.Message):
    await message.answer("Варианты оплаты:")


@user_private_router.message((F.text.lower() == "узнать свой ip"))
@user_private_router.message(Command("2ip"))
async def menu_cmd(message: types.Message):
    await message.answer("Варианты доставки:")
