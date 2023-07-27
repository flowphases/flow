from create_bot import Dispatcher, dp, types, bot, Text
from keyboards.client_kb import ink3, ink6, ink11, ink12


#English


@dp.callback_query_handler(text='en')
async def en_start(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("👋Hello, welcome to the official Oxford International School bot.\n\n💁You can continue by selecting the desired section.", reply_markup=ink3)
    await callback.answer()

#info
@dp.callback_query_handler(text='i_en')
async def i_eng(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_photo(callback.message.chat.id, caption="🏫<b>Oxford International School</b> is a truly innovative learning environment that provides an exceptional level of education for students in <i>9th, 10th and 11th grades.</i>🤩",
    photo='https://t.me/stockexamdep/19', reply_markup=ink6, parse_mode='html')

#Staff
@dp.callback_query_handler(text='p_en')
async def p_eng(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_photo(callback.message.chat.id, photo='https://t.me/stockexamdep/15', protect_content=True, caption="Heloooo", reply_markup=ink12)

#Maqsadimiz
@dp.callback_query_handler(text='m_en')
async def m_eng(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_photo(callback.message.chat.id, photo='https://t.me/stockexamdep/18', protect_content=True, caption="👨‍⚖️<b>Our mission</b>\n\n🎯Formation of a competitive personality with the potential for self-development and self-awareness, ready for full and effective participation in various types of life in a rapidly developing society", reply_markup=ink11, parse_mode='html')


#Back button
@dp.callback_query_handler(Text('b_en'))
async def on_back_to_menu(message):
    await en_start(message)

@dp.callback_query_handler(Text('bb_en'))
async def on_back_to_menu(message):
    await i_eng(message)

@dp.callback_query_handler(Text('ch_en'))
async def on_back_to_menu(message):
    await i_eng(message)