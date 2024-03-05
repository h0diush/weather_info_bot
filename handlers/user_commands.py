from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery

from database import db_helper
from keyboards import get_list_cities_keyboard
from lexicon import LEXICON_RU
from services import get_weather_for_current_city
from state import FMSCity
from utilits import response_to_command_info_city

user_commands = Router()


@user_commands.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(text=LEXICON_RU[message.text])


@user_commands.message(Command(commands='addcity'), StateFilter(default_state))
async def process_add_city_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU[message.text])
    await state.set_state(FMSCity.city)


@user_commands.message(StateFilter(FMSCity.city))
async def process_add_city(message: Message, state: FSMContext):
    city = await db_helper.check_city_in_user(user_id=message.from_user.id,
                                              city=message.text)
    if not city:
        await state.update_data(city=message.text)
        data = await state.get_data()
        await db_helper.insert_city(user_id=message.from_user.id,
                                    city=data["city"])
        await message.answer(text=LEXICON_RU["add_city"])
        await state.clear()
    else:
        await message.answer(text=LEXICON_RU['city_exists'])
        await state.set_state(FMSCity.city)


@user_commands.message(Command(commands='mycities'))
async def process_get_list_cities_current_user(message: Message):
    await message.answer(text=LEXICON_RU[message.text],
                         reply_markup=await get_list_cities_keyboard(
                             message.from_user.id,
                             callback='city',
                             text=''))


@user_commands.callback_query(F.data.startswith('city_'))
async def get_info_the_city(callback: CallbackQuery):
    city_id = int(callback.data.split("_")[1])
    city = await db_helper.get_city_by_id(city_id=city_id)
    info_the_city = await get_weather_for_current_city(city.city)
    if info_the_city:
        await callback.message.answer(
            text=response_to_command_info_city(city=city,
                                               info_the_city=info_the_city)
        )
    else:
        await callback.message.answer(LEXICON_RU["no_city_400"])


@user_commands.message(Command(commands='changecities'))
async def process_change_cities_command(message: Message):
    await message.answer(
        text=LEXICON_RU[message.text],
        reply_markup=await get_list_cities_keyboard(
            message.from_user.id,
            text='❌ ',
            callback='delete'
        )
    )


@user_commands.callback_query(F.data.startswith('delete_'))
async def delete_city(callback: CallbackQuery):
    city_id = int(callback.data.split("_")[1])
    await db_helper.delete_current_city(city_id=city_id)
    await callback.message.answer(LEXICON_RU['delete_city'])
