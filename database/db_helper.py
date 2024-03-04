from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings
from models import User, City


class DatabaseHelper:
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    async def insert_user(self, telegram_id: int, username: str) -> User:
        async with self.session_factory() as session:
            user = await session.scalar(
                select(User).where(User.telegram_id == telegram_id)
            )
            if not user:
                await session.execute(
                    insert(User).values(telegram_id=telegram_id,
                                        username=username)
                )
                await session.commit()

    async def get_current_city(self, user_id: int, city: str) -> City:
        async with self.session_factory() as session:
            city = await session.scalar(
                select(City).filter_by(user_id=user_id, city=city)
            )
            return city

    async def insert_city(self, user_id: int, city: str) -> City:
        async with self.session_factory() as session:
            await session.execute(
                insert(City).values(user_id=user_id,
                                    city=city)
            )
            return await session.commit()


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo
)
