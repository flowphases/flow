from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#Inline Keyboards
ink = InlineKeyboardMarkup(row_width=3)
ib1 = InlineKeyboardButton(text='🇺🇿Uzbek', callback_data='uz')
ib2 = InlineKeyboardButton(text='🇷🇺Russian', callback_data='ru')
ib3 = InlineKeyboardButton(text='🇬🇧English', callback_data='en')

ink.row(ib1, ib2, ib3)

ink1 = InlineKeyboardMarkup(row_width=2)
ink2 = InlineKeyboardMarkup(row_width=2)
ink3 = InlineKeyboardMarkup(row_width=2)
ink4 = InlineKeyboardMarkup(row_width=2)
ink5 = InlineKeyboardMarkup(row_width=2)
ink6 = InlineKeyboardMarkup(row_width=2)
ink7 = InlineKeyboardMarkup(row_width=2)
ink8 = InlineKeyboardMarkup(row_width=2)
ink9 = InlineKeyboardMarkup(row_width=2)
ink10 = InlineKeyboardMarkup(row_width=2)
ink11 = InlineKeyboardMarkup(row_width=2)
ink12 = InlineKeyboardMarkup(row_width=2)
ink13 = InlineKeyboardMarkup(row_width=2)
#Information 
ibt4 = InlineKeyboardButton(text='🤵Ma`lumotlar', callback_data='i_uz')
ibt5 = InlineKeyboardButton(text='🤵O нас', callback_data='i_ru')
ibt6 = InlineKeyboardButton(text='🤵Information', callback_data='i_en')

#Results
ibt7 = InlineKeyboardButton(text='📝Natijalar', callback_data='r_uz')
ibt8 = InlineKeyboardButton(text='📝Результаты', callback_data='r_ru')
ibt9 = InlineKeyboardButton(text='📝Results', callback_data='r_en')

#Back
ibt10 = InlineKeyboardButton(text='◀️Orqaga', callback_data='b_uz')
ibt10_1 = InlineKeyboardButton(text='◀️Orqaga', callback_data='bb_uz')
ibt11 = InlineKeyboardButton(text='◀️Назад', callback_data='b_ru')
ibt11_1 = InlineKeyboardButton(text='◀️Назад', callback_data='bb_ru')
ibt12 = InlineKeyboardButton(text='◀️Back', callback_data='b_en')
ibt12_1 = InlineKeyboardButton(text='◀️Back', callback_data='bb_en')

ink1.row(ibt4, ibt7)
ink2.row(ibt5, ibt8)
ink3.row(ibt6, ibt9)

#Info-Personnel
ibt13 = InlineKeyboardButton(text='🏛Классы', callback_data='p_ru')
ibt14 = InlineKeyboardButton(text='🏛Sinfxonalar', callback_data='x_uz')
ibt15 = InlineKeyboardButton(text='🏛Classrooms', callback_data='p_en')

#Info-Admin
ibt16 = InlineKeyboardButton(text='🤵Admin', url='tg://user?id=851646163')
ibt17 = InlineKeyboardButton(text='🤵Администратор', url='tg://user?id=851646163')

#info-Mission
ibt18 = InlineKeyboardButton(text='🎯Maqsadimiz', callback_data='m_uz')
ibt19 = InlineKeyboardButton(text='🎯Our mission', callback_data='m_en')
ibt20 = InlineKeyboardButton(text='🎯Наша миссия', callback_data='m_ru')

#Add_back
ibt21 = InlineKeyboardButton(text='◀️Chiqish', callback_data='ch_uz')
ibt22 = InlineKeyboardButton(text='◀️Back', callback_data='ch_en')
ibt23 = InlineKeyboardButton(text='◀️Назад', callback_data='ch_ru')
ibt24 = InlineKeyboardButton(text='➡️', callback_data='next')
ibt25 = InlineKeyboardButton(text='⬅️', callback_data='prev')

#To_start
ibt26 = InlineKeyboardButton(text='To start', callback_data='to_start')

ink4.row(ibt13, ibt17).row(ibt20, ibt11)
ink5.row(ibt14, ibt16).row(ibt18, ibt10)
ink6.row(ibt15, ibt16).row(ibt19, ibt12)

#add_back
ink7.row(ibt25, ibt21, ibt24)
ink10.row(ibt25, ibt23, ibt24)
ink12.row(ibt25, ibt22, ibt24)


#Back button one
ink8.row(ibt10_1)
ink9.row(ibt11_1)
ink11.row(ibt12_1)

ink13.row(ibt26)