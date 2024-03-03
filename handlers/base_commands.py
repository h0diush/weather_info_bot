from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon import LEXICON_RU

base_command = Router()


@base_command.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON_RU[message.text])


@base_command.message(Command(commands='help'))
async def process_start_command(message: Message):
    await message.answer(LEXICON_RU[message.text])
