from aiogram import types
import aiogram

from aiogram import Router
from aiogram.filters.command import Command

tg_bot = Router()


@tg_bot.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
