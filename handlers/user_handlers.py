from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import yes_no_kb, test_choice_kb, create_question_kb, main_menu_kb, game_kb
from lexicon.lexicon_ru import LEXICON_RU
from lexicon.questions import all_tests
from database.database import user_dict_template, users_db
from copy import deepcopy
from services.services import *



router = Router()

# Обработчик команды /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'], 
        reply_markup=main_menu_kb
    )
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = user_dict_template.copy()




# Главное меню с кнопками "Выбрать тест", "О проекте", "GitHub", "Оставить отзыв"
@router.message(F.text == LEXICON_RU['start_test'])
async def process_start_test(message: Message):
    await message.answer(
        text=LEXICON_RU['yes'],
        reply_markup=test_choice_kb
    )


# Обработчик кнопки "О проекте"
@router.message(F.text == LEXICON_RU['about_project'])
async def process_about_project(message: Message):
    project_description = (
        "Этот бот помогает пользователю проходить тесты по профориентации и "
        "определять наиболее подходящие карьеры на основе их интересов и склонностей.\n\n"
        "В проекте реализованы различные тесты, включая Тест Климова (ДДО) и другие.\n"
        "Вы можете выбрать тест, пройти его и узнать больше о своих сильных сторонах."
    )
    await message.answer(
        text=project_description,
        reply_markup=main_menu_kb
    )

# Обработчик кнопки "GitHub"
@router.message(F.text == LEXICON_RU['github'])
async def process_github_button(message: Message):
    github_url = "https://github.com/Aydar8888/career_guidance_tg_bot"
    await message.answer(
        text=f"Перейдите по ссылке: {github_url}",
        reply_markup=main_menu_kb
    )


# Обработчик выбора теста
@router.message(F.text.in_([LEXICON_RU['test1'], LEXICON_RU['test2']]))
async def process_test_selection(message: Message):
    selected_test = message.text
    users_db[message.from_user.id]['selected_test'] = selected_test
    users_db[message.from_user.id]['state'] = True
    users_db[message.from_user.id]['question_number'] = 1

    # Очищаем ответы для выбранного теста, если пользователь проходит его заново
    users_db[message.from_user.id]['answers'][selected_test] = []
    
    await send_question(message)

# Функция для отправки вопроса
async def send_question(message: Message):
    user_data = users_db[message.from_user.id]
    selected_test = user_data['selected_test']
    question_number = user_data['question_number']
    
    # Проверяем, не закончен ли тест
    if question_number > len(all_tests[selected_test]):
        # user_data['state'] = False
        # await message.answer(text=LEXICON_RU['end_test'], reply_markup=game_kb)
        # print(users_db[message.from_user.id])
        if question_number > len(all_tests[selected_test]):
            result_message = send_result(message.from_user.id)  # Получаем рекомендации
            await message.answer(text=result_message, reply_markup=game_kb)
            user_data['state'] = False
            
        return

    # Получаем текст вопроса и клавиатуру с вариантами ответа
    question_text = "Что вы предпочтете?"
    options = all_tests[selected_test][question_number]
    question_kb = create_question_kb(options)
    
    await message.answer(text=question_text, reply_markup=question_kb)

# Обработчик для ответов на вопросы
@router.message(F.text.in_([option for test in all_tests.values() for options in test.values() for option in options]))
async def handle_question_answer(message: Message):
    user_data = users_db[message.from_user.id]
    selected_test = user_data['selected_test']
    if not user_data['state']:
        await message.answer("Пожалуйста, начните тест сначала с командой /start.")
        return

    # Сохраняем ответ пользователя в список ответов для текущего теста
    user_data['answers'][selected_test].append(message.text)
    user_data['question_number'] += 1
    await send_question(message)

@router.message(F.text == "Вернуться в главное меню 🔙")
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=main_menu_kb)

# Обработчик отказа от теста
@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'], reply_markup=main_menu_kb)

@router.message(F.text == "Оставить отзыв ✍️")
async def review(message: Message):
    await message.answer(text='https://docs.google.com/forms/u/0/?tgif=d&ec=asw-forms-hero-goto&pli=1')