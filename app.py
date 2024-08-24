import asyncio
from aiogram import Bot, Dispatcher
from handlers.user_group import user_group_router
from dotenv import find_dotenv, load_dotenv
import os
from handlers.user_privet import user_privat_router
from common.bot_command_list import listofcomands
from aiogram.types import BotCommandScopeAllPrivateChats
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()




async def main():
    dp.include_routers(user_privat_router)
    dp.include_routers(user_group_router)
    await bot.set_my_commands(commands=listofcomands, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)
    


asyncio.run(main())

