from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import *
from lexicon.lexicon_ru import LEXICON_RU
from lexicon.questions import question
from database.database import user_dict_template, users_db
from copy import deepcopy


router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)
    


# Этот хэндлер срабатывает на отказ пользователя играть в игру
@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])
    


@router.message(F.text == (LEXICON_RU['test1']))
async def test1(message: Message):
    await message.answer(text=LEXICON_RU['test1_description'], reply_markup=start_back_kb)

user_answers = {}
@router.message(F.text == (LEXICON_RU['start_test']))
async def start_test1(message: Message):
    users_db[message.from_user.id]['state'] = True
    await send_question(1, Message)

# Функция для отправки вопросов с кнопками
async def send_question(question_number, message):
    if question_number > len(questions):
        return

    question_text = f"Вопрос {question_number}: {questions[question_number][0]} или {questions[question_number][1]}?"

    # Создаем клавиатуру с кнопками для вариантов ответов
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text=questions[question_number][0])
    keyboard_builder.button(text=questions[question_number][1])
    keyboard_builder.adjust(1)

    # Отправляем вопрос и клавиатуру
    await message.answer(text=question_text, reply_markup=keyboard_builder)

# Обработчик для ответов на вопросы
@router.message(F.text.in_([option for options in questions.values() for option in options]))
async def handle_answer(message: Message):
    user_id = message.from_user.id
    question_number = len(user_answers[user_id]) + 1

    # Сохраняем ответ пользователя
    user_answers[user_id].append(message.text)

    # Отправляем следующий вопрос
    await send_question(user_id, question_number + 1)



@router.message(F.text == (LEXICON_RU['back']))
async def back(message: Message):
    await message.answer(reply_markup=game_kb)




# async def process_game_button(message: Message):
#     bot_choice = get_bot_choice()
#     await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
#                               f'- {LEXICON_RU[bot_choice]}')
#     winner = get_winner(message.text, bot_choice)
#     await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)