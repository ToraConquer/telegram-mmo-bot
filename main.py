import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart

# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)

# Получаем токен бота из переменной окружения
# Это безопасный способ хранить токен, мы настроим его на сервере
API_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Создаем объекты бота и диспетчера
# Объект Bot - это наш бот, через него мы будем отправлять сообщения
# Объект Dispatcher - "мозг" бота, он решает, какая функция должна ответить на сообщение
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Этот блок будет выполняться, когда пользователь отправит команду /start
@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    """
    Этот хэндлер (обработчик) будет отправлять приветственное сообщение
    в ответ на команду /start
    """
    await message.reply("Привет! Я - заготовка для будущей MMORPG. Скоро здесь будет игра!")

async def main():
    # Запускаем бота и ждем входящие сообщения
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
