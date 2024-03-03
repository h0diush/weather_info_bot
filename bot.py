import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import load_config_bot, ConfigBot

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
               "[%(asctime)s] - %(name)s - %(message)s",
    )
    logger.info("starting Bot...")
    config: ConfigBot = load_config_bot()
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
