import asyncio                                   # - для работы с асинхронностью
import config                                    # - для подлкючения файла confing
from aiogram import Bot, Dispatcher, types, F
import logging
from handlers import common, survey

async def main():
    # Включаем логгирование
    logging.basicConfig(level=logging.INFO)

    # Создаем объект бота
    bot = Bot(token=config.token)

    # Диспечер
    dp = Dispatcher()

    dp.include_router(survey.router)
    dp.include_router(common.router)


    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())