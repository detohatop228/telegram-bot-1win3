import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import executor

API_TOKEN = 'YOUR_TOKEN_HERE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

ref_button = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text="🔥 Нова гра!", url="https://lhcets.life/?open=register&app=cczh")
)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привіт! Багато хто питає, як я заробляю з телефону 📱\n\n"
        "Ось ігрова біржа – без верифікації, швидкі виплати!\n"
        "👆 Тисни кнопку, щоб спробувати!",
        reply_markup=ref_button
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
