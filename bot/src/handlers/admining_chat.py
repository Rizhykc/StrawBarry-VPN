from aiogram import Bot, Router, types
from aiogram.filters import Command

list_router = Router()


@list_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    admin_list = await bot.get_chat_administrators(chat_id)

    admin_list = [
        member.user.id
        for member in admin_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.admins_list = admin_list
    if message.from_user.id in admin_list:
        await message.delete()
