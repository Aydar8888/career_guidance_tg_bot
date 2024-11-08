from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import yes_no_kb, test_choice_kb, create_question_kb
from lexicon.lexicon_ru import LEXICON_RU
from lexicon.questions import all_tests
from database.database import user_dict_template, users_db
from copy import deepcopy


router = Router()

# Обработчик команды /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)

# Обработчик согласия на участие в тесте
@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=test_choice_kb)

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
        user_data['state'] = False
        await message.answer(text=LEXICON_RU['end_test'])
        print(users_db[message.from_user.id])
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

# Обработчик отказа от теста
@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'], reply_markup=yes_no_kb)