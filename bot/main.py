import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import find_dotenv, load_dotenv

from const import ALLOWED_UPDATES
from src.common.bot_cmds_list import private
from src.database.engine import create_db, drop_db, session_maker
from src.handlers.admin_private import admin_router
from src.handlers.admining_chat import list_router
from src.handlers.user_private import user_router
from src.middlewares.db import DataBaseSession

load_dotenv(find_dotenv())

bot = Bot(
    token=os.getenv('TOKEN'),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

bot.admins_list = []
dp = Dispatcher()

dp.include_router(user_router)
dp.include_router(admin_router)
dp.include_router(list_router)


async def on_startup(bot):

    run_param = False
    if run_param:
        await drop_db()

    await create_db()


async def on_shutdown(bot):
    print('Бот лег поспать!')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private,
                              scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == "__main__":
    asyncio.run(main())
