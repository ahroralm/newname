import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types
import json
import requests



token = '5703438899:AAHQdIQwvpQIEKVwNpWHK-l2anKKNFaPBL8'
bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn.add('USD-UZS', 'RUB-UZS', 'TRY-UZS',)


@dp.message_handler(commands=['start'])
async def first(message: types.Message):
    rasm1 = open('rasm/1ci.png','rb')
    cap = f'As-Salomu alakum marhamat ozingizga kerak bolimni tanlang '
    await bot.send_photo(message.chat.id, rasm1, caption=cap, reply_markup=btn)


@dp.message_handler(content_types=['text'])
async def second(message: types.Message):
    global inputs, outputs, result, cap, rasm
    text = message.text
    if text == 'USD-UZS':
        await bot.send_message(message.chat.id,'Dollarda summani kriting : ')
        inputs = 'USD'
        outputs = 'UZS'
        rasm = open('rasm/usduzs.jpg', 'rb')
        cap = f'Bu Kiritgan summangizni somdagi qiymati :'
    if text == 'RUB-UZS':
        await bot.send_message(message.chat.id,'Rublda summani kritng :')
        inputs = 'RUB'
        outputs = 'UZS'
        rasm = open('rasm/rubuzs.jpg', 'rb')
        cap = f'Bu Kiritgan summangizni somdagi qiymati :'
    if text == 'TRY-UZS':
        inputs = 'TRY'
        outputs = 'UZS'
        rasm = open('rasm/tryuzs.jpg', 'rb')
        cap = f'Bu Kiritgan summangizni somdagi qiymati :'
        await bot.send_message(message.chat.id, 'Lirada summani kriting :')
    url = 'https://v6.exchangerate-api.com/v6/4896d51961595bb59a0b1ef0/latest/'+ inputs
    response = requests.get(url)
    b = json.loads(response.text)
    result = b['conversion_rates']['UZS']
    if message.text.isdigit():
        print(int(message.text) * result)
        await bot.send_photo(message.chat.id, rasm, caption=cap)
        await bot.send_message(message.chat.id, int(message.text) * result)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
