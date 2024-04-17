import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKKEN
from app.handlers import router



async def main():
    bot = Bot(token=TOKKEN)
    dp = Dispatcher()
    dp.include_routers(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')