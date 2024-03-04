from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from models import Base, int_pk


class City(Base):
    __tablename__ = 'cities'

    id: Mapped[int_pk]
    city: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.telegram_id"))
    user: Mapped["User"] = relationship()
