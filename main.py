import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
import logging
from handlers import start,random_recipe,myinfo,dishes
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types
from aiogram import Router
from handlers.dishes import shop_router
from handlers.start import start_router
from handlers.myinfo import my_info_router
from bot_config import bot, dp




#
# async def start_handler(message: types Message):
# # print(message.from_user)
# # await message,answer (f"Привет, (message.from_user.first_name}*)
# kb = types.InLineKeyboardMarkupC
# inline_keyboard=[
# [
# types. InlineKeyboardButton(text="Haw c", Url="https://geeks.kg"),
# types. InlineKeyboardButton(text="Наш инстеграм", Url="https://instagram.com/geeks.kg"),
# await message.reply(f"Привет.
# (message-from_user first_name}", reply_markup=kb)




# @dp.message(commands=['start'])
# async def send_welcome(message: types.Message):
#     await message.reply("Приветствую вас!")
async def main():
    # регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(shop_router)
    dp.include_router(my_info_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


