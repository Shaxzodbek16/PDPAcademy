import asyncio
import logging
import sys
import json
from textwrap import indent

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

import environ

environ.Env.read_env('../.env')
env = environ.Env()
BOT_TOKEN = env('BOT_TOKEN')
TOKEN = BOT_TOKEN
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    answer = 'Hello, you have a chance to control you group with \'Control bot\'\n'
    answer += 'Add me your group, and I will never let the people get bored !'
    answer += 'Add your group and give me admin permission.'
    await message.answer(answer)


@dp.message()
async def any_message_handler(msg: Message) -> None:
    question_text = msg.reply_to_message
    answer_text = msg.text
    if 'jasur' in answer_text:
        await msg.reply('Yana Jasurmi??')
    with open('messages.json', 'r') as f:
        messages = json.load(f)
    if question_text:
        question_text = question_text.text
        if not question_text in messages.keys():
            messages[question_text.lower()] = answer_text.lower()
            with open('messages.json', 'w') as f:
                json.dump(messages, f, indent=3)
    if answer_text in messages.keys():
        await msg.reply((messages.get(answer_text)))


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
