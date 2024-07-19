# from aiogram import Router, types
# from aiogram.filters.command import Command
#
# picture_router = Router()
#
#
# @picture_router.message(Command("picture"))
# async def picture_handler(message: types.Message):
#     image = types.FSInputFile("image/images.jpg")
#     await message.answer_photo(
#         photo=image,
#         caption="Интереснейшая книга"
#     )
#
from aiogram import Router, F, types


shop_router = Router()


@shop_router.message(F.text == "хоррор")
async def horror_handler(message: types.Message):
    await message.answer("Книги жанра хоррор")


@shop_router.message(F.text == "фантастика")
async def fantasy_handler(message: types.Message):
    await message.answer("Книги жанра фантастика")