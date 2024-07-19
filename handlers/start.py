# from aiogram.filters.command import Command
# from aiogram import types
# from aiogram import Dispatcher
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# kb = InlineKeyboardButton,InlineKeyboardMarkup
#
# @dp.message(Command('keyboard'))
# async def send_keyboard(message: types.Message):
# async def send_welcome(message: types.Message):
#     kb = types.InlineKeyboardMarkup(
#         InlineKeyboardMarkup=[
#             [
#                 types.InlineKeyboardButton(text="наш адрес", callback_data="address"),
#                 types.InlineKeyboardButton(text="контакты", callback_data="0700376054"),
#                 types.InlineKeyboardButton(text="о нас", callback_data="about_us"),
#                 types.InlineKeyboardButton(text="Наш сайт", url="https://youtu.be/cUjbapoU3x0?si=qLg9IaRzBeG5xLGY"),
#                 types.InlineKeyboardButton(text="", callback_data="feedback"),
#                 types.InlineKeyboardButton(text="Наши вакансии", callback_data="jobs")
#             ]
#         ]
#     )
#     await message.render(f"hi, {message.from_user.first_name}", reply_markup=kb)
#
#
#
# async def send_welcome(message: types.Message):
#     await message.reply(f"Привет, {message.from_user.first_name}!")
#
# def register_handlers(dp: Dispatcher):
#     dp.message(send_welcome, commands=['start'])
# # @dp.message(Command("start"))
# # async def send_welcome(message: types.Message):
#     await message.reply(f"Привет, {message.from_user.first_name}!")
from aiogram.filters import Command
from aiogram import Router, F, types

start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    # print(message.from_user)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
            ],
            [
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/geeks.kg"),
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us"),
            ],
            [
                types.InlineKeyboardButton(text="Пожертвуйте нам", callback_data="donate_us"),
            ]
        ]
    )
    await message.answer(
        text=f"Привет, {message.from_user.first_name},  я бот, который поможет вам выбрать и купить книгу в нашем магазине.",
        reply_markup=kb
    )


@start_router.callback_query(F.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    await callback.message.answer("О нас")



@start_router.callback_query(F.data == "donate_us")
async def donate_us(callback: types.CallbackQuery):
    await callback.message.answer("Спасибо за поддержку! ")