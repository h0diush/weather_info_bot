from aiogram import Bot
from aiogram.types import BotCommand

from lexicon import MENU_BOT


async def set_menu_bot(bot: Bot):
    menu_bot = [BotCommand(command=command, description=description) for
                command, description in MENU_BOT.items()]
    await bot.set_my_commands(menu_bot)
