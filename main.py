import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import logging
import random

recipes = [
    "Рецепт 1: \n1. Ингредиент А\n2. Ингредиент Б\n3. Ингредиент В\n4. Приготовление: смешать все и готовить 20 минут.",
    "Рецепт 2: \n1. Ингредиент Г\n2. Ингредиент Д\n3. Ингредиент Е\n4. Приготовление: запекать при 180 градусах 30 минут.",
    "Рецепт 3: \n1. Ингредиент Ж\n2. Ингредиент З\n3. Ингредиент И\n4. Приготовление: варить 10 минут на слабом огне.",
    "Рецепт 4: \n1. Ингредиент К\n2. Ингредиент Л\n3. Ингредиент М\n4. Приготовление: обжарить на среднем огне 15 минут.",
    "Рецепт 5: \n1. Ингредиент Н\n2. Ингредиент О\n3. Ингредиент П\n4. Приготовление: тушить 25 минут под крышкой."
]

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply(f"Привет, {message.from_user.first_name}!")

@dp.message(Command('myinfo'))
async def send_myinfo(message: types.Message):
    user_info = (
        f"Ваш ID: {message.from_user.id}\n"
        f"Ваше имя: {message.from_user.first_name}\n"
        f"Ваш username: {message.from_user.username}"
    )
    await message.reply(user_info)

@dp.message(Command('random_recipe'))
async def send_random_recipe(message:types.Message):
    recipe = random.choice(recipes)
    await message.answer(recipe)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.run_polling(bot)


