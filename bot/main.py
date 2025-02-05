import asyncio
import os

from aiogram import Bot, Dispatcher, types
from const import ALLOWED_UPDATES
from dotenv import load_dotenv

from src.common.bot_cmds_list import private
from src.handlers.admin_private import admin_router
from src.handlers.admining_chat import list_router
from src.handlers.user_private import user_router

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
bot.admins_list = []
dp = Dispatcher()

dp.include_router(user_router)
dp.include_router(admin_router)
dp.include_router(list_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private,
                              scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == "__main__":
    asyncio.run(main())
