from datetime import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase, mapped_column

int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"))]


class Base(DeclarativeBase):
    __abstract__ = True
