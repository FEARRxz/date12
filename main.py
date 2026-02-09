import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup

BOT_TOKEN = "8251143975:AAH8A7dW-g5SIMpzKzLcQwv92dwtrSbWpHc"

START_TEXT = (
    "Годовщина 🌸\n\n"
    "📅 Дата: 12.02.26\n"
    "⏰ Время: 15:00\n"
    "📍 Место: Tanuki Шевченко 98\n"
    "👗 Дресс код: в свою любимую и красивую одежду 😍\n\n"
    "Буду очень рад тебя видеть жаным ❤️💫"
)

ADDRESS_TEXT = (
    "🍱Tanuki Шевченко 98🍣\n"
    "Чтобы было удобно вот ссылка🥰 : "
    '<a href="https://2gis.kz/almaty/geo/70000001078526241">ТЫК</a>'
)

BTN_ANNIVERSARY = "Годовщина 🌸"
BTN_ADDRESS = "Адрес 📍"

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=BTN_ANNIVERSARY), KeyboardButton(text=BTN_ADDRESS)]],
    resize_keyboard=True,
    one_time_keyboard=False,
    selective=False,
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
    if not token:
        raise RuntimeError("Вставь реальный токен бота в переменную BOT_TOKEN в main.py")

    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    asyncio.run(main())
