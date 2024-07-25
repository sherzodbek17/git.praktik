from aiogram import types, Bot, Dispatcher, filters, F
import asyncio
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import openai


bot = Bot(token="7087348224:AAHu_F9cFxAEPcHCymniDoOIA4deo566aFg")
dp = Dispatcher(bot=bot)


openai.api_key = ""

class Reg_uzb(StatesGroup):
    ism = State()
    raqam = State()

class Reg_rus(StatesGroup):
    name = State()
    number = State()


order = []
order_ru = []

lst = []
list = []



lang_set = [
    [KeyboardButton(text="Ru"), KeyboardButton(text="Uz")]
]

set_lang = ReplyKeyboardMarkup(keyboard=lang_set, resize_keyboard=True)


contact_button_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Kontakt jo'natish", request_contact=True)]
], resize_keyboard=True)
contact_button_ru = ReplyKeyboardMarkup( keyboard=[
    [KeyboardButton(text="Поделиться контактом", request_contact=True)]
], resize_keyboard=True)


uz_menu = [
    [KeyboardButton(text="Kurs"), KeyboardButton(text="Korzinka"), KeyboardButton(text="Biz haqimizda")],
    [KeyboardButton(text="Qollab quvatlash"), KeyboardButton(text="Til sozlamalari")]
]

menu_uz = ReplyKeyboardMarkup(keyboard=uz_menu, resize_keyboard=True)

ru_menu = [
    [KeyboardButton(text="Курс"),  KeyboardButton(text="Корзинка") ,KeyboardButton(text="О нас")],
    [KeyboardButton(text="Поддержка"), KeyboardButton(text="Поменять язык")]
]

menu_ru = ReplyKeyboardMarkup(keyboard=ru_menu, resize_keyboard=True)



kurs_menu = [
[KeyboardButton(text="Dizayn"), KeyboardButton(text="Frontend")],
[KeyboardButton(text="Backend"), KeyboardButton(text="Orqaga")]
]

uz_kurs = ReplyKeyboardMarkup(keyboard=kurs_menu, resize_keyboard=True)

kurs_menu_ru = [
[KeyboardButton(text="Дизайн"), KeyboardButton(text="Фронтэнд")],
[KeyboardButton(text="Бэкенд"), KeyboardButton(text="Назад")]
]

ru_kurs = ReplyKeyboardMarkup(keyboard=kurs_menu_ru, resize_keyboard=True)


dizayn_uz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Dizayn 3 oy", callback_data="d3")],
    [InlineKeyboardButton(text="Dizayn 6 oy", callback_data="d6")],
    [InlineKeyboardButton(text="Dizayn 1 yil", callback_data="d1")]
])

dizayn_ru = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Дизайн 3 месяца", callback_data="д3")],
    [InlineKeyboardButton(text="Дизайн 6 месяца", callback_data="д6")],
    [InlineKeyboardButton(text="Дизайн 1 года", callback_data="д1")]
])


frontend_uz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Frontend 3 oy", callback_data="f3")],
    [InlineKeyboardButton(text="Frontend 1 yil", callback_data="f1")]
])

frontend_ru = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Фронтэнд 3 месяца", callback_data="ф3")],
    [InlineKeyboardButton(text="Фронтэнд 1 года", callback_data="ф1")]
])


backend_uz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Backend 5 oy", callback_data="b3")],
    [InlineKeyboardButton(text="Backend 1 yil", callback_data="b1")]
])

backend_ru = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Бакенд 5 месяца", callback_data="б3")],
    [InlineKeyboardButton(text="Бакенд 1 года", callback_data="б1")]
])


buy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Qoshish ➕", callback_data="plus")],
    [InlineKeyboardButton(text="Orqaga 🔙", callback_data="ortga")]
])

kup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Добавить ➕", callback_data="dobavit")],
    [InlineKeyboardButton(text="Назад 🔙", callback_data="nazad")]
])


savat  = []
korzina = []


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    savat.clear()
    await message.answer("Xush kelibsiz\nTilni Tanlang - Выберите язык", reply_markup=set_lang)



@dp.message(F.text=="Ru")
async def reg1(message: types.Message, state: FSMContext):
    await state.set_state(Reg_rus.name)
    await message.answer('Введите ваше имя')


@dp.message(Reg_rus.name)
async def reg2(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg_rus.number)
    await state.set_state(Reg_rus.number)
    await message.answer('Введите номер телефона',  reply_markup=contact_button_ru)


@dp.message(Reg_rus.number)
async def two_three(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Спасибо, Вы прошли регистрацию\nИмя:  {data["name"]}\nНомер:  {data["number"]}", reply_markup=menu_ru)
    await state.clear()



@dp.message(F.text=="Uz")
async def reg_uzz(message: types.Message, state: FSMContext):
    await state.set_state(Reg_uzb.ism)
    await message.answer('Ismizni kiriting: ')


@dp.message(Reg_uzb.ism)
async def reg_uzb(message: types.Message, state: FSMContext):
    await state.update_data(ism=message.text)
    await state.set_state(Reg_uzb.raqam)
    await message.answer('Telefon raqamingizni kiriting: ', reply_markup=contact_button_uz)


@dp.message(Reg_uzb.raqam)
async def two_three_uzb(message: types.Message, state: FSMContext):
    await state.update_data(raqam=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Siz muvaffaqaiyatli royxatdan otdingiz\nIsm:  {data["ism"]}\nTel raqam:  {data["raqam"]}", reply_markup=menu_uz)
    await state.clear()


@dp.message(F.text =="Kurs")
async def start_function(message: types.Message):
    await message.answer("Bizni kurslarimiz", reply_markup=uz_kurs)


@dp.message(F.text =="Курс")
async def start_function(message: types.Message):
    await message.answer("Наши курсы", reply_markup=ru_kurs)


@dp.message(F.text =="Dizayn")
async def start_function(message: types.Message):
    await message.answer("Dizayn kursi tariflari", reply_markup=dizayn_uz)


@dp.message(F.text =="Дизайн")
async def start_function(message: types.Message):
    await message.answer("Тарифы по дизайн", reply_markup=dizayn_ru)


@dp.message(F.text =="Backend")
async def start_function(message: types.Message):
    await message.answer("Backend kursi tariflari", reply_markup=backend_uz)


@dp.message(F.text =="Бэкенд")
async def start_function(message: types.Message):
    await message.answer("Тарифы по Бакенд", reply_markup=backend_ru)

@dp.message(F.text =="Frontend")
async def start_function(message: types.Message):
    await message.answer("Frontend kursi tariflari", reply_markup=frontend_uz)


@dp.message(F.text =="Фронтэнд")
async def start_function(message: types.Message):
    await message.answer("Тарифы по фронтенд", reply_markup=frontend_ru)



@dp.callback_query(F.data =="d3")
async def start_function(calllback: CallbackQuery):
    d3p = "https://www.guvi.in/blog/wp-content/uploads/2023/10/ui-ux-tools-1200x675.webp"
    lst.append("Dizayn 3 oy")
    list.append("Дизайн 3 месяца")
    await calllback.message.answer_photo(photo=d3p, caption=f"Dizayn 3 oy \nNarxi: 140 $", reply_markup=buy)


@dp.callback_query(F.data =="d6")
async def start_function(calllback: CallbackQuery):
    d3p = "https://www.esearchlogix.com/wp-content/uploads/2024/01/UI-and-UX-Design.jpg"
    lst.append("Dizayn 6 oy ")
    list.append("Дизайн 6 месяца")
    await calllback.message.answer_photo(photo=d3p, caption=f"Dizayn 6 oy \nNarxi: 200 $", reply_markup=buy)


@dp.callback_query(F.data =="d1")
async def start_function(calllback: CallbackQuery):
    d3p = "https://miro.medium.com/v2/resize:fit:682/1*j7TiBo6BraFMeXme9BHCcw.jpeg"
    lst.append("Dizayn 1 yil")
    list.append("Дизайн 1 год")
    await calllback.message.answer_photo(photo=d3p, caption=f"Dizayn 1 yil \nNarxi: 250 $", reply_markup=buy)


@dp.callback_query(F.data =="д3")
async def start_function(calllback: CallbackQuery):
    d3p = "https://www.guvi.in/blog/wp-content/uploads/2023/10/ui-ux-tools-1200x675.webp"
    lst.append("Dizayn 3 oy")
    list.append("Дизайн 3 месяца")
    await calllback.message.answer_photo(photo=d3p, caption=f"Дизайн 3 месяца \nЦена: 140 $", reply_markup=kup)


@dp.callback_query(F.data =="д6")
async def start_function(calllback: CallbackQuery):
    d3p = "https://www.esearchlogix.com/wp-content/uploads/2024/01/UI-and-UX-Design.jpg"
    lst.append("Dizayn 6 oy")
    list.append("Дизайн 6 месяца")
    await calllback.message.answer_photo(photo=d3p, caption=f"Дизайн 6 месяца \nЦена: 200 $", reply_markup=kup)


@dp.callback_query(F.data =="д1")
async def start_function(calllback: CallbackQuery):
    d3p = "https://miro.medium.com/v2/resize:fit:682/1*j7TiBo6BraFMeXme9BHCcw.jpeg"
    lst.append("Dizayn 1 yil ")
    list.append("Дизайн 1 год")
    await calllback.message.answer_photo(photo=d3p, caption=f"Дизайн 1 год \nЦена: 250 $", reply_markup=kup)



@dp.callback_query(F.data =="f3")
async def start_function(calllback: CallbackQuery):
    f3p = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8RbrPwU5HxqkakRGDM-d30_VUH-fKLyJMUQ&s"
    lst.append("Frontend 5 oy")
    list.append("Фронтенд 5 месяца ")
    await calllback.message.answer_photo(photo=f3p, caption=f"Frontend 5 oy \nNarxi: 140 $", reply_markup=buy)


@dp.callback_query(F.data =="f1")
async def start_function(calllback: CallbackQuery):
    f1p = "https://camo.githubusercontent.com/a926e5ed4e795ff94c4fa30da05db86d1cfe3cf7f5c2b21a49f3a5ddc63067a0/68747470733a2f2f7777772e6b696e64706e672e636f6d2f706963632f6d2f3239392d323939343031315f66726f6e742d656e642d646576656c6f706d656e742d6c6f676f732d68642d706e672d646f776e6c6f61642e706e67"
    lst.append("Frontend 1 yil")
    list.append("Фронтенд 1 года ")
    await calllback.message.answer_photo(photo=f1p, caption="Frontend 1 yil \nNarxi: 270 $", reply_markup=buy)



@dp.callback_query(F.data =="ф3")
async def start_function(calllback: CallbackQuery):
    f3p = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8RbrPwU5HxqkakRGDM-d30_VUH-fKLyJMUQ&s"
    lst.append("Frontend 5 oy")
    list.append("Фронтенд 5 месяца ")
    await calllback.message.answer_photo(photo=f3p, caption=f"Фронтенд 5 месяца \nЦена: 140 $", reply_markup=kup)



@dp.callback_query(F.data =="ф1")
async def start_function(calllback: CallbackQuery):
    f1p = "https://camo.githubusercontent.com/a926e5ed4e795ff94c4fa30da05db86d1cfe3cf7f5c2b21a49f3a5ddc63067a0/68747470733a2f2f7777772e6b696e64706e672e636f6d2f706963632f6d2f3239392d323939343031315f66726f6e742d656e642d646576656c6f706d656e742d6c6f676f732d68642d706e672d646f776e6c6f61642e706e67"
    lst.append("Frontend 1 yil")
    list.append("Фронтенд 1 год")
    await calllback.message.answer_photo(photo=f1p, caption=f"Фронтенд 1 год \nЦена: 270 $", reply_markup=kup)



@dp.callback_query(F.data =="b3")
async def start_function(calllback: CallbackQuery):
    b1p = "https://hblabgroup.com/wp-content/uploads/2022/06/lap-trinh-backend.png"
    lst.append("Backend  5 oy")
    list.append("Бакенд  5 месяца")
    await calllback.message.answer_photo(photo=b1p, caption="Backend  5 oy \nNarxi: 140 $", reply_markup=buy)



@dp.callback_query(F.data =="b1")
async def start_function(calllback: CallbackQuery):
    b3p = "https://www.quytech.com/blog/wp-content/uploads/2024/01/top-backend-frameworks-for-app-development.png"
    lst.append("Backend 1 yil")
    list.append("Бакенд 1 год")
    await calllback.message.answer_photo(photo=b3p, caption=f"Backend 1 yil \nNarxi: 300 $", reply_markup=buy)


@dp.callback_query(F.data =="б3")
async def start_function(calllback: CallbackQuery):
    b1p = "https://hblabgroup.com/wp-content/uploads/2022/06/lap-trinh-backend.png"
    lst.append("Backend 5 oy")
    list.append("Бакенд 5 месяца ")
    await calllback.message.answer_photo(photo=b1p, caption="Бакенд  5 месяца \nNarxi: 140 $", reply_markup=buy)



@dp.callback_query(F.data =="б1")
async def start_function(calllback: CallbackQuery):
    b3p = "https://www.quytech.com/blog/wp-content/uploads/2024/01/top-backend-frameworks-for-app-development.png"
    lst.append("Backend 1 yil")
    list.append("Бакенд 1 год")
    await calllback.message.answer_photo(photo=b3p, caption=f"Бакенд 1 год \nNarxi: 300 $", reply_markup=kup)



@dp.callback_query(F.data=="ortga")
async def add(calllback: CallbackQuery):
    await calllback.message.answer(reply_markup=uz_kurs)

@dp.callback_query(F.data=="nazad")
async def add(calllback: CallbackQuery):
    await calllback.message.answer(reply_markup=ru_kurs)


@dp.message(F.text=="Orqaga")
async def reg1(message: types.Message):
    await message.answer('Siz menyudasiz', reply_markup=menu_uz)



@dp.message(F.text=="Поменять язык")
async def reg1(message: types.Message):
    await message.answer('Выберите язык', reply_markup=set_lang)


@dp.message(F.text=="Til sozlamalari")
async def reg1(message: types.Message):
    await message.answer('Tilni tanlang', reply_markup=set_lang)



@dp.message(F.text=="Назад")
async def reg1(message: types.Message):
    await message.answer('Вы вернулись', reply_markup=menu_ru)


@dp.message(F.text=="Qollab quvatlash")
async def reg1(message: types.Message):
    chat = "https://cionews.co.in/wp-content/uploads/2023/04/Article-Main-Image-46.png"
    await message.answer_photo(photo=chat, caption="Ooops! Ayrim sabablarga kora Chat-Gpt vaqtinchalik ishlamayapti, tez orada ishlab ketadi :)")


@dp.message(F.text=="Поддержка")
async def reg1(message: types.Message):
    chat = "https://cionews.co.in/wp-content/uploads/2023/04/Article-Main-Image-46.png"
    await message.answer_photo(photo=chat, caption="Упс! Chat-Gpt временно недоступен по каким-то причинам, скоро заработает :)")


@dp.message(F.text=="Biz haqimizda")
async def reg1(message: types.Message):
    await message.answer("Biz proweb kompaniyasi dasturchilarni ishga olyamiz \nBatafsil: https://proweb.uz/")


@dp.message(F.text=="О нас")
async def reg1(message: types.Message):
    await message.answer("Приглашаем на работу программистов в компанию proweb \nПодробнее: https://proweb.uz/")



@dp.callback_query(F.data == "plus")
async def cancel(callback: CallbackQuery):
    order.append(lst[-1])
    await callback.answer(text=f"{callback.from_user.full_name} Sizni buyurtmangiz qabul qilindi.")


@dp.callback_query(F.data == "dobavit")
async def cancel(callback: CallbackQuery):
    order_ru.append(list[-1])
    await callback.answer(text=f"{callback.from_user.full_name} Ваш заказ успешно принят.")


@dp.message(F.text==("Korzinka"))
async def start(message: types.Message):
    if order:
        await message.answer(f"Sinzing zakazingiz: {', '.join(order)}")

    else:
        await message.answer("Sizda xali buyurtma yoq")


@dp.message(F.text==("Корзинка"))
async def start(message: types.Message):
    if order_ru:
        await message.answer(f"Ваши заказы: {', '.join(order_ru)}")

    else:
        await message.answer("Вы не заказали еще")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
