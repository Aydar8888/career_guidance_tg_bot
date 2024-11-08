from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU
from lexicon.questions import questions

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# ------- Создаем игровую клавиатуру без использования билдера -------

# Создаем кнопки игровой клавиатуры
button_1 = KeyboardButton(text=LEXICON_RU['test1'])
button_2 = KeyboardButton(text=LEXICON_RU['test2'])
button_3 = KeyboardButton(text=LEXICON_RU['test3'])
start_test = KeyboardButton(text=LEXICON_RU['start_test'])
back = KeyboardButton(text=LEXICON_RU['back'])

start_back_kb = ReplyKeyboardMarkup(
    keyboard=[[start_test],
              [back]],
    resize_keyboard=True
)

game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3]],
    resize_keyboard=True
)


buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i}') for i in questions.values()]

keyboard: list[list[KeyboardButton]] = [
    [buttons[0:1]]
]
my_keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)



