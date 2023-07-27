from aiogram import types
from create_bot import dp, bot, Dispatcher
from database.data_base import cursor, conn


#@dp.message_handler()
async def logic(message: types.Message):
    await message.answer(f"Botda {message.text} deb nomlangan buyruq yo'q. Iltimos berilgan buyruqlardan foydalaning")



@dp.message_handler()
async def results(message: types.Message):
    info = cursor.execute("SELECT * FROM `marks` WHERE ois = '{key}'".format(key=message.text))

    items = info.fetchall()


    for item in items:
        if message.text not in (info):
            await bot.send_message(message.chat.id, "Please check your OIS-ID\nIltimos OIS-ID ni tekshirib qaytadan kiriting.")
    
        else:
            await bot.send_message(message.chat.id, 
            f"MONTHLY REPORT\n------------------------------------\nOIS-ID:\t\t{item[1]}\nMonth:\t\t{item[2]}\nResult:\t\t{item[3]}\nScholarship:\t\t{item[4]}\n------------------------------------\nMath:\t\t{item[5]}\nPhysics:\t\t{item[6]}\nHistory:\t\t{item[7]}\nRussian:\t\t{item[8]}\nEnglish:\t\t{item[9]}\nLiterature:\t\t{item[10]}\nComputer:\t\t{item[11]}\nGeography:\t\t{item[12]}", protect_content=True)

#Register handlers
def register_handlers_other(dp: Dispatcher):
   dp.register_message_handler(logic)
   dp.register_message_handler(results)
