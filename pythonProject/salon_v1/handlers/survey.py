from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.survey_keyboards import make_row_keyboard


router = Router()


response1 = ['18-25', '25-45', '45+']
response2 = ['Скорость', 'Тренды', 'Роскошь', 'Профессионализм']
response3 = ['Маникюр/Педикюр', 'Цвет волос/Прически', 'SPA/Mассаж', 'Макияж/Стрижка']
response4 = ['Онлайн', 'Звонок', 'Личное посещение', 'Рекомендация']
response5 = ['Расслабление', 'Мода', 'Молодость', 'Услуги']
response6 = ['Уют', 'Технологии', 'Профессионализм', 'Персонализация']

class SurveyResponse(StatesGroup):
     survey_response1 = State()
     survey_response2 = State()
     survey_response3 = State()
     survey_response4 = State()
     survey_response5 = State()
     survey_response6 = State()


# Хендлер на команду /signup
@router.message(Command('survey'))
@router.message(Command('опрос'))
async def cmd_resp1(message: types.Message, state: FSMContext):
     name = message.chat.first_name
     await message.answer(f'{name}, Пожалуйста, выбирайте варианты ответов, нажимая на соответствующие кнопки.'
                          f'Ваш отклик поможет нам лучше понять ваши предпочтения. Благодарим за участие!'
                          )
     await message.answer(f'{name}, выберите Ваш возраст.', reply_markup=make_row_keyboard(response1))
     await state.set_state(SurveyResponse.survey_response1)



@router.message(SurveyResponse.survey_response1, F.text.in_(response1))
async def cmd_resp2(message: types.Message, state: FSMContext):
     name = message.chat.first_name
     await state.update_data(s_r1=message.text.lower())
     await message.answer(f'Спасибо, а теперь ответьте на вопрос.\n{name}, что для вас наиболее важно?', reply_markup=make_row_keyboard(response2))
     await state.set_state(SurveyResponse.survey_response2)

@router.message(SurveyResponse.survey_response1)
async def cmd_resp1_incorrectly(message: types.Message):
     await message.answer(f'Я не знаю такого ответа.', reply_markup=make_row_keyboard(response1))



@router.message(SurveyResponse.survey_response2, F.text.in_(response2))
async def cmd_resp2(message: types.Message, state: FSMContext):
     name = message.chat.first_name
     await state.update_data(s_r2=message.text.lower())
     await message.answer(f'Спасибо, а теперь ответьте на вопрос.\n{name}, какие услуги вы предпочитаете?', reply_markup=make_row_keyboard(response3))
     await state.set_state(SurveyResponse.survey_response3)

@router.message(SurveyResponse.survey_response2)
async def cmd_resp2_incorrectly(message: types.Message):
     await message.answer(f'Я не знаю такого ответа.', reply_markup=make_row_keyboard(response2))



@router.message(SurveyResponse.survey_response3, F.text.in_(response3))
async def cmd_resp3(message: types.Message, state: FSMContext):
     name = message.chat.first_name
     await state.update_data(s_r3=message.text.lower())
     await message.answer(f'Спасибо, а теперь ответьте на вопрос.\n{name}, какой способ записи для Вас удобный??', reply_markup=make_row_keyboard(response4))
     await state.set_state(SurveyResponse.survey_response4)

@router.message(SurveyResponse.survey_response3)
async def cmd_resp3_incorrectly(message: types.Message):
     await message.answer(f'Я не знаю такого ответа.', reply_markup=make_row_keyboard(response3))



@router.message(SurveyResponse.survey_response4, F.text.in_(response4))
async def cmd_resp4(message: types.Message, state: FSMContext):
     name = message.chat.first_name
     await state.update_data(s_r4=message.text.lower())
     await message.answer(f'Спасибо, а теперь ответьте на вопрос.\n{name}, какая из следующих характеристик салона красоты для вас наиболее важна?', reply_markup=make_row_keyboard(response5))
     await state.set_state(SurveyResponse.survey_response5)

@router.message(SurveyResponse.survey_response4)
async def cmd_resp4_incorrectly(message: types.Message):
     await message.answer(f'Я не знаю такого ответа.', reply_markup=make_row_keyboard(response4))



@router.message(SurveyResponse.survey_response5, F.text.in_(response5))
async def cmd_resp5(message: types.Message, state: FSMContext):
     name = message.chat.first_name
     await state.update_data(s_r5=message.text.lower())
     await message.answer(f'Спасибо, а теперь ответьте на вопрос.\n{name}, какая из следующих характеристик салона красоты для вас наиболее значима?', reply_markup=make_row_keyboard(response6))
     await state.set_state(SurveyResponse.survey_response6)

@router.message(SurveyResponse.survey_response5)
async def cmd_resp5_incorrectly(message: types.Message):
     await message.answer(f'Я не знаю такого ответа.', reply_markup=make_row_keyboard(response5))



@router.message(SurveyResponse.survey_response6, F.text.in_(response6))
async def cmd_resp5(message: types.Message, state: FSMContext):
     name = message.chat.first_name
     user_data = await state.get_data()
     await message.answer(
          f'Привет!'
          f'\nМы рады видеть тебя в нашем салоне красоты!'
          f'\nТы выбрала {user_data.get('s_r2')} как приоритет, что значит, что наши мастера всегда сделают все качественно.'
          f'\nТвой выбор услуг - {user_data.get('s_r3')} - позволит тебе получить невероятные результаты.'
          f'\nДля записи ты выбрала {user_data.get('s_r4')}, что гарантирует тебе легкость и удобство при заказе услуг.'
          f'\nТвоя основная причина посещения - {user_data.get('s_r5')}'
          f'\nНаша ключевая характеристика - {message.text.lower()}!'
          f'\nЖдем тебя в нашем салоне!', reply_markup=types.ReplyKeyboardRemove())
     await state.clear()

@router.message(SurveyResponse.survey_response6)
async def cmd_resp6_incorrectly(message: types.Message):
     await message.answer(f'Я не знаю такого ответа.', reply_markup=make_row_keyboard(response6))
