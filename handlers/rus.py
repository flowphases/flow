from create_bot import dp, bot, Dispatcher, types
from keyboards.client_kb import ink, ink1, ink2, ink3, ink4, ink7, ink9, ink10
from aiogram.dispatcher.filters import Text
from database.data_base import conn, cursor

#Start
@dp.message_handler(commands=["start"])
async def first(message: types.Message,):
    await message.answer("🇺🇿 Botni ishlatishda davom etish uchun tilni tanlang.\n\n🇬🇧 To continue using the bot, select a language\n\n🇷🇺 Выберите язык, чтобы продолжить использование бота", reply_markup=ink)


#Additional start
@dp.callback_query_handler(text='ibt26')
async def add_first(callback: types.CallbackQuery):
    await callback.message.answer("🇺🇿 Botni ishlatishda davom etish uchun tilni tanlang.\n\n🇬🇧 To continue using the bot, select a language\n\n🇷🇺 Выберите язык, чтобы продолжить использование бота", reply_markup=ink)

#Russian
@dp.callback_query_handler(text='ru')
async def ru_start(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("👋Здравствуйте, добро пожаловать на официальный бот Oxford International School.\n\n💁Вы можете продолжить, выбрав нужный раздел.", reply_markup=ink2)
    await callback.answer()

#Info
@dp.callback_query_handler(text='i_ru')
async def i_rus(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_photo(callback.message.chat.id, caption="🏫<b>Oxford International School</b> — это действительно инновационная учебная среда, которая обеспечивает исключительно высокий уровень образования для учащихся <i>9, 10 и 11 классов.</i>🤩", parse_mode='html',
    photo='https://t.me/stockexamdep/19', reply_markup=ink4)

#Staff
@dp.callback_query_handler(text='p_ru')
async def p_rus(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_photo(callback.message.chat.id, photo='https://t.me/stockexamdep/15', protect_content=True, caption="Sardor Vakhobov", reply_markup=ink10)

#about us
@dp.callback_query_handler(text='m_ru')
async def m_rus(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_photo(callback.message.chat.id, photo='https://t.me/stockexamdep/18', protect_content=True, caption="Формирование конкурентоспособной личности, обладающей потенциалом саморазвития и самосознания, готовой к полноценному и эффективному участию в различных типах жизни в стремительно развивающемся обществе.", reply_markup=ink9)


#Results
@dp.callback_query_handler(text='r_ru')
async def m_rus(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_message(callback.message.chat.id, "Please insert your OIS ID")


#Back button
@dp.callback_query_handler(Text('ch_ru'))
async def on_back_to_menu(message):
    await i_rus(message)

@dp.callback_query_handler(Text('b_ru'))
async def on_back_to_menu(message):
    await ru_start(message)

@dp.callback_query_handler(Text('bb_ru'))
async def on_back_to_menu(message):
    await i_rus(message)


#Register handlers.
def register_handlers_rus(dp: Dispatcher):
    dp.register_message_handler(first, commands=['start'])
