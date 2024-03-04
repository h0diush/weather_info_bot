from typing import Union

from sqlalchemy.orm import Mapped, relationship

from models import Base, int_pk


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int_pk]
    username: Mapped[Union[str]]
    # created_at: Mapped[created_at]  # для postgresql
    cities: Mapped[list["City"]] = relationship()
