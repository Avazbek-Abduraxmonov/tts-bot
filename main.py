from aiogram import Bot, Dispatcher, types
from asyncio import run
from aiogram.filters import Command
from function import *
from config import *

dp = Dispatcher()

async def startAnswer(bot: Bot):
    await bot.send_message(chat_id=admin_id, text="Bot ishga tushdi ✅")

async def shutdownAnswer(bot: Bot):
    await bot.send_message(chat_id=admin_id , text="Bot ishdan to'xtadi ❌")

async def start():
    dp.startup.register(startAnswer)
    dp.message.register(startCommandAnswer, Command('start'))
    dp.message.register(textAnswerAudio)
    dp.shutdown.register(shutdownAnswer)

    bot = Bot(token=token)
    await dp.start_polling(bot, polling_timeout=1)

run(start())