import asyncio
import os

from tg_insert_data import tg_bot
from aiogram import Bot, Dispatcher


ALOWED_UPDATES = ["message"]

token = '6537139791:AAG-dkwUAvH3HhpTlMEAQQ9KMS2lV3ErTzY'

bot = Bot(token=token)
dp = Dispatcher()

dp.include_router(tg_bot)



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALOWED_UPDATES)


asyncio.run(main())