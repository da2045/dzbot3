from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
from filters.chat_filters import ChatTypeFilter
import random
from common.function import get_random_dog


answers = ["Hello! how are you?", "Hi there!","Hey!","Howdy!","Greetings!","What’s up?"]
gritings = ["hi", "Hello", "hello","Hi","what's up","What's  up"]
user_privat_router = Router()
user_privat_router.message.filter(ChatTypeFilter(['private']))




@user_privat_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello {message.from_user.full_name} to you")

@user_privat_router.message(F.photo)
async def get_photo(message:Message):
    await message.reply("this is photo but i need some text to help you")

@user_privat_router.message(Command('photo'))
async def cmd_photo(message:Message):
    message.reply('what photo you want')
    res = message.text
    await message.answer_photo()
#dorobit
@user_privat_router.message(Command('dog'))
async def cmd_dog(message:Message):
    await message.answer_photo(get_random_dog())

@user_privat_router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("i am a simple bot that can greet you")

@user_privat_router.message(F.text == "Hello")
async def answer_hello(message: Message):
    await message.answer("Hello how are you?")

@user_privat_router.message(F.text.in_(gritings))
async def answer_hello(message: Message):
    await message.answer(answers[random.randint(0,6)])