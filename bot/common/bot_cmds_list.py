import utils.const as txt
from aiogram.filters import Command, CommandStart
from aiogram.types import BotCommand, Message

from Button import kbds_users as kb
from handlers.user_private import user_router

private = [
    BotCommand(command='start', description='Перезапуск бота'),
    BotCommand(command='help', description='Памагитэ'),
]


@user_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.reply(f'Привет! {message.from_user.first_name}\n {txt.TEXT}',
                        reply_markup=kb.main_inline)


@user_router.message(Command('help'))
async def help_admin(message: Message):
    await message.reply(text=txt.ADMIN_HELP,
                        reply_markup=kb.main_inline)
