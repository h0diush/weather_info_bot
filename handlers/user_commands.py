from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message

from database import db_helper
from lexicon import LEXICON_RU
from state import FMSCity

user_commands = Router()


@user_commands.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(LEXICON_RU[message.text])


@user_commands.message(Command(commands='addcity'), StateFilter(default_state))
async def process_add_city_command(message: Message, state: FSMContext):
    await message.answer(LEXICON_RU[message.text])
    await state.set_state(FMSCity.city)


@user_commands.message(StateFilter(FMSCity.city))
async def process_add_city(message: Message, state: FSMContext):
    city = await db_helper.get_current_city(user_id=message.from_user.id,
                                            city=message.text)
    if not city:
        await state.update_data(city=message.text)
        data = await state.get_data()
        await db_helper.insert_city(user_id=message.from_user.id,
                                    city=data["city"])
        await message.answer(LEXICON_RU["add_city"])
        await state.clear()
    else:
        await message.answer(LEXICON_RU['city_exists'])
        await state.set_state(FMSCity.city)

