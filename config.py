from aiogram import types, Bot, Dispatcher, filters, F
import asyncio
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import openai
import exam


bot = Bot(token="7087348224:AAHu_F9cFxAEPcHCymniDoOIA4deo566aFg")
dp = Dispatcher(bot=bot)


dizayn_3 = 120
dizayn_6 = 180
dizayn_1 = 240

savat  = []
korzina = []


@dp.callback_query(F.data =="d3")
async def start_function(calllback: CallbackQuery):
    d3p = "https://www.guvi.in/blog/wp-content/uploads/2023/10/ui-ux-tools-1200x675.webp"
    await calllback.message.answer_photo(photo=d3p , caption=f"Dizayn 3 oy \nNarxi: {dizayn_3} $")

@dp.callback_query(F.data =="d6")
async def start_function(calllback: CallbackQuery):
    d3p = "https://www.guvi.in/blog/wp-content/uploads/2023/10/ui-ux-tools-1200x675.webp"
    await calllback.message.answer_photo(photo=d3p , caption=f"Dizayn 6 oy \nNarxi: {dizayn_6} $")

@dp.callback_query(F.data =="d1")
async def start_function(calllback: CallbackQuery):
    d3p = "https://www.guvi.in/blog/wp-content/uploads/2023/10/ui-ux-tools-1200x675.webp"
    await calllback.message.answer_photo(photo=d3p , caption=f"Dizayn 1 yil \nNarxi: {dizayn_1} $")





async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
