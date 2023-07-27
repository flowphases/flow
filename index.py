from aiogram import executor
from create_bot import dp
from handlers import eng, rus, uz, other
from database import data_base

async def on_startup(_):
    data_base.sql_start()

#Import registered handlers
rus.register_handlers_rus(dp)
other.register_handlers_other(dp)

#Execute
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)