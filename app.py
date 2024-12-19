import asyncio
import os

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

from const import ALLOWED_UPDATES
from common.bot_cmds_list import private
from handlers.user_private import user_private_router

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_private_router)



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == "__main__":
    asyncio.run(main())
