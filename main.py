import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

import keyboards as kb

from dotenv import load_dotenv
import os
import random

load_dotenv()
bot = Bot(os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Выберите действие:', reply_markup=kb.startMenu)

@dp.message(F.text == 'Назад')
async def backToMainMenu(message: Message):
    await message.answer('Выберите действие:', reply_markup=kb.startMenu)

@dp.message(F.text == 'Случайная книга')
async def rand(message: Message):
    await message.answer(f"Рандомное число: {random.randint(1000, 10000)}")

@dp.message(F.text == 'Информация')
async def info(message: Message):
    await message.answer('Ссылки', reply_markup=kb.urlsMenu)


@dp.message(F.text.in_(['Меню']))
async def submenu(message: Message):
    await message.answer('Выберите действие:', reply_markup=kb.subMenu)

@dp.message()
async def echo(message: Message):
    await message.answer(message.text)



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

