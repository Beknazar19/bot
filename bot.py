import asyncio
import logging

import pandas as pd

from aiogram import Bot, Dispatcher, types
from clickhouse_driver import Client
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
# from keyboards import keyboard
from aiogram.types import Message, ContentType
from aiogram.types.webhook_info import  WebhookInfo
# from aiogram.types.message import web_app_data

logging.basicConfig(
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
)



APP_TOKEN = "5870615975:AAHsfWlYVdHgyIa_dnPjBQaDiik3ujNZUKk"

# Initialize bot and dispatcher
# bot = Bot(token=os.environ.get(APP_TOKEN))
bot = Bot(token=APP_TOKEN)

dp = Dispatcher(bot)
path_ads = "https://beknazar19.github.io/ads.github.io/"
path_search = "https://jazzy-puppy-bc95fe.netlify.app/"





def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
    keyboard = types.ReplyKeyboardMarkup(row_width=1) #создаем клавиатуру
    web_app_ads = WebhookInfo(url=path_ads)
    web_app_search = WebhookInfo(url=path_search)

    one_butt = types.KeyboardButton(text="Дать объявление", web_app=web_app_ads) #создаем кнопку типа webapp
    two_butt = types.KeyboardButton(text="Найти объявлений", web_app=web_app_search) #создаем кнопку типа webapp
    keyboard.add(one_butt, two_butt) #добавляем кнопки в клавиатуру
    # keyboard.add(one_butt)
    return keyboard #возвращаем клавиатуру

def webAppKeyboardInline(): #создание inline-клавиатуры с webapp кнопкой
   keyboard = types.InlineKeyboardMarkup(row_width=1) #создаем клавиатуру inline
   web_app_ads = WebhookInfo(url=path_ads)
   one = types.InlineKeyboardButton(text="Веб приложение", web_app=web_app_ads) #создаем кнопку типа webapp
   keyboard.add(one) #добавляем кнопку в клавиатуру
   return keyboard #возвращаем клавиатуру



@dp.message_handler(Command('start'))
async def start(message: Message):
# async def start(payload: types.Message):
    await bot.send_message(message.chat.id,
                           'Тестируемся WebApp',
                           reply_markup=webAppKeyboard())


@dp.message_handler(Command('zzz_for_test'))
async def webz(web_app_message):
    answer_data = web_app_message
# async def start(payload: types.Message):
    print("data: ", answer_data) 




@dp.message_handler(content_types="web_app_data") #получаем отправленные данные 
async def answer(web_app_message):    
    print("data: ", web_app_message)  #конкретно то что мы передали в бота
    await bot.send_message(web_app_message.chat.id, f"получили информацию из веб-приложения: {web_app_message.web_app_data.data}")

#    отправляем сообщение в ответ на отправку данных из веб-приложения 




if __name__=="__main__":
    executor.start_polling(dp)

