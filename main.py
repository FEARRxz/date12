import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from aiogram.client.default import DefaultBotProperties

# Токен: берём из ENV (Railway) или из строки ниже
BOT_TOKEN = os.getenv("BOT_TOKEN") or "PUT_NEW_TOKEN_HERE"

START_TEXT = (
    "Годовщина 🌸\n\n"
    "📅 Дата: 12.02.26\n"
    "⏰ Время: 16:00\n"
    "📍 Место: Penka, Сейфуллина 574/6\n"
    "👗 Дресс код: в свою любимую и красивую одежду 😍\n\n"
    "Буду очень рад тебя видеть жаным ❤️💫"
)

ADDRESS_TEXT = (
    "Penka, Сейфуллина 574/6\n"
    "Чтобы было удобно вот ссылка🥰 : "
    '<a href="https://2gis.kz/almaty/geo/70000001087539898">ТЫК</a>'
)

BTN_ANNIVERSARY = "Годовщина 🌸"
BTN_ADDRESS = "Адрес 📍"

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=BTN_ANNIVERSARY), KeyboardButton(text=BTN_ADDRESS)]],
    resize_keyboard=True,
)


dp = Dispatcher()


@dp.message(Command("start"))
async def handle_start(message: Message) -> None:
    await message.answer("Привет Асылнур👋❤️", reply_markup=main_keyboard)


@dp.message(Command("adress"))
async def handle_adress(message: Message) -> None:
    await message.answer(ADDRESS_TEXT, reply_markup=main_keyboard)


@dp.message(lambda m: m.text and m.text.casefold() == BTN_ANNIVERSARY.casefold())
async def handle_anniversary_button(message: Message) -> None:
    await message.answer(START_TEXT, reply_markup=main_keyboard)


@dp.message(lambda m: m.text and m.text.casefold() == BTN_ADDRESS.casefold())
async def handle_address_button(message: Message) -> None:
    await message.answer(ADDRESS_TEXT, reply_markup=main_keyboard)


async def main() -> None:
    token = BOT_TOKEN.strip()
    if not token or token == "PUT_NEW_TOKEN_HERE":
        raise RuntimeError("Укажи реальный токен бота в BOT_TOKEN или переменной окружения")

    # Правильная инициализация для aiogram 3.7+
    bot = Bot(
        token=token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    asyncio.run(main())
