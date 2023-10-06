from aiogram import Bot, Dispatcher, types, executor
from logging  import basicConfig , INFO

from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

basicConfig(level=INFO)

start_keyboards = [
    types.KeyboardButton("О нас"),
    types.KeyboardButton("Объекты"),
    types.KeyboardButton("Контакты")
]

start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer(f"ДОБРО ПОЖАЛОВАТЬ НА НАШУ КОМПАНИЮ {message.from_user.full_name}",reply_markup=start_button)

@dp.message_handler(text="О нас")
async def about(message:types.Message):
    await message.answer("""ОсОО «Визион Групп»
Мы - развивающаяся компания, которая предлагает своим клиентам широкий выбор квартир в объектах расположенных во всех наиболее привлекательных районах городов Ош и Джалал-Абад. У нас максимально выгодные условия, гибкий (индивидуальный) подход при реализации жилой и коммерческой недвижимости. Мы занимаем лидирующие позиции по количеству объектов по югу Кыргызстана. Наша миссия: Мы обеспечиваем население удобным жильем для всей семьи, проявляя лояльность и индивидуальный подход и обеспечивая высокий уровень обслуживания. Мы обеспечиваем бизнес подходящим коммерческим помещением, используя современные решения и опыт профессионалов своего дела.
                         

Почему выбирают нас?


Широкий выбор
Мы предоставляем самый широкий выбор жилой и коммерческой недвижимости в городах Ош и Джалал-Абад.
                         
Индивидуальный подход к каждому клиенту
У нас есть возможность подобрать то, что нужно каждому клиенту

                         
Прозрачная и честная тарификация
Вы напрямую покупаете недвижимость у застройщика без посредников.

                         
Мы заботимся о своей репутации
Нам важно, чтобы вы, становясь нашим клиентом, были довольны.

""")

@dp.message_handler(text ="Объекты")
async def objects(message:types.Message):
    await message.answer_photo("https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_1260,h_708/https://vg-stroy.com/wp-content/uploads/2022/01/dji_0392-scaled-1.jpeg")
    await message.answer("""ЖК «Малина-Лайф»
г.Ош, ул Монуева 19""")
    await message.answer_photo("https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_873,h_1280/https://vg-stroy.com/wp-content/uploads/2022/01/2022-02-09-14.22.41.jpg")
    await message.answer("""ЖК «Томирис»
г. Ош, ул. Аматова 1 (ориентир - Драм. театр)""")
    await message.answer_photo("https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_1260,h_708/https://vg-stroy.com/wp-content/uploads/2022/01/dji_0289-scaled-1.jpeg")
    await message.answer("""ЖК «Черемушки»
г.Ош, ул. Урицкого 15Б""")
    await message.answer_photo("https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_1000,h_562/https://vg-stroy.com/wp-content/uploads/2022/01/frunze.jpeg")
    await message.answer("""ЖК «Фрунзе»
г.Ош, Ленина 170""")
    

@dp.message_handler(text="Контакты")
async def contacts(message:types.Message):
    await message.answer("""г.Ош, ул.Аматова 1, Бизнес центр Томирис

contact@vg-stroy.com
+996 709 620088
+996 772 620088
+996 550 620088
""")

executor.start_polling(dp)