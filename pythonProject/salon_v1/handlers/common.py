from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from keyboards.keyboards import kb1, kb2


router = Router()


# Хендлер на команду /start
@router.message(Command('start'))
@router.message(Command('старт'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Здравствуйте, {name}!')
    await message.answer(f'Я бот, который здесь для того, чтобы помочь вам с вашими запросами, записью на услуги и ответами на ваши вопросы.', reply_markup=kb1)

# Хендлер на команду /master
@router.message(Command('master'))
@router.message(Command('мастер'))
async def cmd_master(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'{name}, для какой услуги Вам требуется мастер?', reply_markup=kb2)

# Хендлер на команду /service
@router.message(Command('service'))
@router.message(Command('услуги'))
async def cmd_master(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'{name}, вот перечень услуг оказываемых нашим салоном красоты')
    await message.answer(f'Парикмахерские услуги\n\nСтрижки\nОкрашивание\nУкладки\nЛаминирование\выпрямление\n\nНогтевой сервис\n\nМаникюр\nПедикюр\nНаращивание ногтей\nДизайн ногтей\n\nКосметологические услуги\n\nЧистки\nМассажи\nОмолаживающие процедуры\nИнъекции\n\nСПА-услуги\n\nОбертывания\nСПА-программы', reply_markup=kb2)

# Хендлер на команду /price
@router.message(Command('price'))
@router.message(Command('цена'))
async def cmd_price(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'В настоящее время данный раздел находится на стадии разработки. Со всеми акутальными ценами вы можете ознакомиться в нашем салоне по адресу: г.Москва, ул.Большая Садовая, д.1')

# Хендлер на команду /сontact
@router.message(Command('contact'))
@router.message(Command('контакты'))
async def cmd_сontact(message: types.Message):
     name = message.chat.first_name
     await message.answer(f'Мы находимся по адресу: г.Москва, ул.Большая Садовая, д.1\nТелефон: +1 123 456 78 90\nE-mail: trio@bs.com\nНаш сайт: http://triobs.tilda.ws')

# Хендлер на команду /signup
@router.message(Command('signup'))
@router.message(Command('запись'))
async def cmd_сontact(message: types.Message):
     name = message.chat.first_name
     await message.answer(f'В настоящее время данный раздел находится на стадии разработки. Вы можете записаться к нам по телефону: +1 123 456 78 90\nE-mail: trio@bs.com')

# Хендлер на команду /home
@router.message(Command('home'))
@router.message(Command('главная'))
async def cmd_home(message: types.Message):
     name = message.chat.first_name
     await message.answer(f'{name}, возращаем, Вас в начало', reply_markup=kb1)

# Хендлер на команду /stop
@router.message(Command('stop'))
@router.message(Command('стоп'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Спасибо, что воспользовались нашими услугами! Если у вас возникнут еще вопросы или потребуется помощь, не стесняйтесь обращаться. Ждем вас снова в нашем салоне красоты! До скорой встречи! 💖')



# Хендлер на сообщения
@router.message(F.text)
async def cmd_master(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'мастер' in msg_user:
        await message.answer(f'{name}, для какой услуги Вам требуется мастер?', reply_markup=kb2)
    elif 'мастера' in msg_user:
        await message.answer(f'{name}, для какой услуги Вам требуется мастер?', reply_markup=kb2)
    elif 'услуга' in msg_user:
        await message.answer(f'{name}, вот перечень услуг оказываемых нашим салоном красоты')
        await message.answer(f'Парикмахерские услуги\n\nСтрижки\nОкрашивание\nУкладки\nЛаминирование\выпрямление\n\nНогтевой сервис\n\nМаникюр\nПедикюр\nНаращивание ногтей\nДизайн ногтей\n\nКосметологические услуги\n\nЧистки\nМассажи\nОмолаживающие процедуры\nИнъекции\n\nСПА-услуги\n\nОбертывания\nСПА-программы', reply_markup=kb2)
    elif 'услуги' in msg_user:
        await message.answer(f'{name}, вот перечень услуг оказываемых нашим салоном красоты')
        await message.answer(f'Парикмахерские услуги\n\nСтрижки\nОкрашивание\nУкладки\nЛаминирование\выпрямление\n\nНогтевой сервис\n\nМаникюр\nПедикюр\nНаращивание ногтей\nДизайн ногтей\n\nКосметологические услуги\n\nЧистки\nМассажи\nОмолаживающие процедуры\nИнъекции\n\nСПА-услуги\n\nОбертывания\nСПА-программы', reply_markup=kb2)
    elif 'цена' in msg_user:
        await message.answer(f'В настоящее время данный раздел находится на стадии разработки. Со всеми акутальными ценами вы можете ознакомиться в нашем салоне по адресу: г.Москва, ул.Большая Садовая, д.1')
    elif 'прайс' in msg_user:
        await message.answer(f'В настоящее время данный раздел находится на стадии разработки. Со всеми акутальными ценами вы можете ознакомиться в нашем салоне по адресу: г.Москва, ул.Большая Садовая, д.1')
    elif 'стоимость' in msg_user:
        await message.answer(f'В настоящее время данный раздел находится на стадии разработки. Со всеми акутальными ценами вы можете ознакомиться в нашем салоне по адресу: г.Москва, ул.Большая Садовая, д.1')
    elif 'контакты' in msg_user:
        await message.answer(f'Мы находимся по адресу: г.Москва, ул.Большая Садовая, д.1\nТелефон: +1 123 456 78 90\nE-mail: trio@bs.com\nНаш сайт: http://triobs.tilda.ws', reply_markup=kb2)
    elif 'телефон' in msg_user:
        await message.answer(f'Мы находимся по адресу: г.Москва, ул.Большая Садовая, д.1\nТелефон: +1 123 456 78 90\nE-mail: trio@bs.com\nНаш сайт: http://triobs.tilda.ws', reply_markup=kb2)
    elif 'адрес' in msg_user:
        await message.answer(f'Мы находимся по адресу: г.Москва, ул.Большая Садовая, д.1\nТелефон: +1 123 456 78 90\nE-mail: trio@bs.com\nНаш сайт: http://triobs.tilda.ws', reply_markup=kb2)
    elif 'где найти' in msg_user:
        await message.answer(f'Мы находимся по адресу: г.Москва, ул.Большая Садовая, д.1\nТелефон: +1 123 456 78 90\nE-mail: trio@bs.com\nНаш сайт: http://triobs.tilda.ws', reply_markup=kb2)
    elif 'как позвонить' in msg_user:
        await message.answer(f'Мы находимся по адресу: г.Москва, ул.Большая Садовая, д.1\nТелефон: +1 123 456 78 90\nE-mail: trio@bs.com\nНаш сайт: http://triobs.tilda.ws', reply_markup=kb2)
    elif 'запиши' in msg_user:
        await message.answer(f'В настоящее время данный раздел находится на стадии разработки. Вы можете записаться к нам по телефону: +1 123 456 78 90\nE-mail: trio@bs.com')
    elif 'запись' in msg_user:
        await message.answer(f'В настоящее время данный раздел находится на стадии разработки. Вы можете записаться к нам по телефону: +1 123 456 78 90\nE-mail: trio@bs.com')
    elif 'главное меню' in msg_user:
        await message.answer(f'Возращаем, Вас в начало', reply_markup=kb1)
    elif 'главная' in msg_user:
        await message.answer(f'Возращаем, Вас в начало', reply_markup=kb1)
    elif 'меню' in msg_user:
        await message.answer(f'Возращаем, Вас в начало', reply_markup=kb1)
