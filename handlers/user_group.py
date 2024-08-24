from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
from filters.chat_filters import ChatTypeFilter
import random

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


bad_words = {'bad', 'word', 'bad_word', 'badword'}

@user_group_router.message()
@user_group_router.edited_message()
async def check_words(message:Message):
    if bad_words.intersection(set(message.text.lower().split())):
        await message.delete()
        await message.answer("you can't use this message here")