from create_bot import Dispatcher, dp, types, bot, Text
from keyboards.client_kb import ink1, ink, ink5, ink7, ink8

#Uzbek
@dp.callback_query_handler(text='uz')
async def uz_start(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("👋Assalomu aleykum Oxford International School rasmiy botiga xush kelibsiz.\n\n💁Kerakli bo'limni tanlab davom etishingiz mumkin.", reply_markup=ink1)
    await callback.answer()

#info
@dp.callback_query_handler(text='i_uz')
async def i_uzbek(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_photo(callback.message.chat.id, caption="🏫<b>Oxford International School</b>\n9, 10 va 11-sinf o`quvchilariga g`ayrioddiy yuqori ta`lim standartlarini taqdim etuvchi chinakkam innovatsion o`quv muhitidir.🤩",
    photo='https://t.me/stockexamdep/19', reply_markup=ink5, parse_mode='html')

#Staff
@dp.callback_query_handler(text='x_uz')
async def x_uzbek(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_photo(callback.message.chat.id, photo='https://t.me/stockexamdep/15', protect_content=True, caption="Heloooo", reply_markup=ink7)

#Maqsadimiz
@dp.callback_query_handler(text='m_uz')
async def m_uzbek(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_photo(callback.message.chat.id, photo='https://t.me/stockexamdep/18', protect_content=True, caption="👨‍⚖️<b>Bizning maqsadimiz</b>\n\n🎯O’z-o’zini rivojlantirish va o’zini o’zi anglash salohiyatiga ega, jadal rivojlanayotgan jamiyatda hayotning turli turlarida to’liq va samarali ishtirok etishga tayyor raqobatbardosh shaxsni shakllantirish.", reply_markup=ink8, parse_mode='html')



#Back button
@dp.callback_query_handler(Text('b_uz'))
async def on_back_to_menu(message):
    await uz_start(message)

@dp.callback_query_handler(Text('bb_uz'))
async def on_back_to_menu(message):
    await i_uzbek(message)

@dp.callback_query_handler(Text('ch_uz'))
async def on_back_to_menu(message):
    await i_uzbek(message)

