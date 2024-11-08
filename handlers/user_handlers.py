from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb, start_back_kb, my_keyboard
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

@router.message(F.text == (LEXICON_RU['start_test']))
async def start_test1(message: Message):
    users_db[message.from_user.id]['state'] = True
    await message.answer(text=question['const_question'])
    await message.answer(reply_markup=my_keyboard)
    
        


@router.message(F.text == (LEXICON_RU['back']))
async def back(message: Message):
    await message.answer(reply_markup=game_kb)




# async def process_game_button(message: Message):
#     bot_choice = get_bot_choice()
#     await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
#                               f'- {LEXICON_RU[bot_choice]}')
#     winner = get_winner(message.text, bot_choice)
#     await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)