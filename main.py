import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
import logging
from handlers import start,random_recipe,myinfo,dishes
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types
from aiogram import Router
from handlers.dishes import dishes_router
from handlers.start import start_router
from handlers.myinfo import my_info_router
from bot_config import bot, dp
from handlers.review_dialog import review_dialog_router


async def main():
    # регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(dishes_router)
    dp.include_router(my_info_router)
    dp.include_router(review_dialog_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


