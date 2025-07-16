import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import executor

API_TOKEN = '7790542897:AAEhKs-_vTB11-Uqq0BjHJqFWgRoEFUb0DE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

ref_button = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text="🎁 Забрати подарунок", url="https://1whecs.life/?open=register&p=cczw")
)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привіт! Багато хто питає, як я заробляю з телефону 📱\n\n"
        "Ось ігрова біржа – без верифікації, та з мега швидкими виплатами!\n\n"
        "🔥Реєструйся – бонус вже чекає💸\n\n"
        "👇 Тисни кнопку, щоб спробувати! 👇",
        reply_markup=ref_button
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
