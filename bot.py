from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart
import asyncio

# Замените на токен вашего бота
TOKEN = "8070699664:AAEMGr3TM0KsvGTfkwqSASaWhZQc1sKOg2w"

# Создание бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда старт
@dp.message(CommandStart())
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть Mini App",
                    web_app=WebAppInfo(url="https://tg-mini-app-7qi3.onrender.com")
                )
            ]
        ]
    )
    await message.answer(
        "Привет! Это Mini App. Нажми кнопку ниже, чтобы начать 🚀",
        reply_markup=keyboard
    )

# Функция запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
