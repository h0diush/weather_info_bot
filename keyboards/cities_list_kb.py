from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database import db_helper


async def get_list_cities_keyboard(user_id: int, callback: str,
                                   text: str = '') -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    cities = await db_helper.get_cities_user(user_id=user_id)
    for city in cities:
        kb_builder.row(
            InlineKeyboardButton(
                text=f'{text}{city.city}',
                callback_data=f"{callback}_{city.id}"
            )
        )
    return kb_builder.as_markup()
