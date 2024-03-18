from aiogram import Bot, Dispatcher, types
import asyncio
import logging
import config
from aiogram.utils import executor
from aiogram.utils.exceptions import BotBlocked

logging.basicConfig(level=logging.INFO, format='\033[33m {}'.format('%(name)s %(levelname)s: %(message)s'))

# TOKEN = getenv("TOKEN")
TOKEN = config.TOKEN
# if not TOKEN:
#     exit("Error: no token provided")
proxy_url = 'http://proxy.server:3128'
bot = Bot(token=TOKEN, proxy=proxy_url)


dp = Dispatcher(bot)


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"Пользователь заблокировал бота \n Сообщение: {update}\nОшибка: {exception}")
    return True


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await asyncio.sleep(10.0)
    user_name = message.from_user.full_name
    await message.answer(f"Привет, {user_name}!\n Это учебный эхо бот")


@dp.message_handler(commands=['about'])
async def cmd_about(message: types.Message):
    await message.answer("Я просто повторяю твои сообщения")


@dp.message_handler()
async def cmd(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp)
