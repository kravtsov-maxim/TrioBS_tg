from aiogram import types

button1 = types.KeyboardButton(text='Мастера')
button2 = types.KeyboardButton(text='Услуги')
button3 = types.KeyboardButton(text='Цена')
button4 = types.KeyboardButton(text='Контакты')
button5 = types.KeyboardButton(text='/опрос')
button6 = types.KeyboardButton(text='Главное меню')
button7 = types.KeyboardButton(text='Запись')



button1_1 = types.KeyboardButton(text='Парикмахерская')
button1_2 = types.KeyboardButton(text='Ногтевой сервис')
button1_3 = types.KeyboardButton(text='Косметология')
button1_4 = types.KeyboardButton(text='СПА')


keyboard1 = [
    [button5],
    [button1, button2],
    [button3, button4],
    [button7],
]



keyboard2 = [
    [button1_1, button1_2],
    [button1_3, button1_4],
    [button6]
]



kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)