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

# Генерируем список с кнопками
buttons1: list[KeyboardButton] = [
    KeyboardButton(text=i[0]) for i in questions.values()]
buttons2: list[KeyboardButton] = [
    KeyboardButton(text=i[1]) for i in questions.values()]

keyboard1: list[list[KeyboardButton]] = [
    [buttons1[0],
     buttons2[0]]
]
keyboard2: list[list[KeyboardButton]] = [
    [buttons1[1],
     buttons2[1]]
]
keyboard3: list[list[KeyboardButton]] = [
    [buttons1[2],
     buttons2[2]]
]
keyboard4: list[list[KeyboardButton]] = [
    [buttons1[3],
     buttons2[3]]
]
keyboard5: list[list[KeyboardButton]] = [
    [buttons1[4],
     buttons2[4]]
]
keyboard6: list[list[KeyboardButton]] = [
    [buttons1[5],
     buttons2[5]]
]
keyboard7: list[list[KeyboardButton]] = [
    [buttons1[6],
     buttons2[6]]
]
keyboard8: list[list[KeyboardButton]] = [
    [buttons1[7],
     buttons2[7]]
]
keyboard9: list[list[KeyboardButton]] = [
    [buttons1[8],
     buttons2[8]]
]
keyboard10: list[list[KeyboardButton]] = [
    [buttons1[9],
     buttons2[9]]
]
keyboard11: list[list[KeyboardButton]] = [
    [buttons1[10],
     buttons2[10]]
]
keyboard12: list[list[KeyboardButton]] = [
    [buttons1[11],
     buttons2[11]]
]
keyboard13: list[list[KeyboardButton]] = [
    [buttons1[12],
     buttons2[12]]
]
keyboard14: list[list[KeyboardButton]] = [
    [buttons1[13],
     buttons2[13]]
]
keyboard15: list[list[KeyboardButton]] = [
    [buttons1[14],
     buttons2[14]]
]
keyboard16: list[list[KeyboardButton]] = [
    [buttons1[15],
     buttons2[15]]
]
keyboard17: list[list[KeyboardButton]] = [
    [buttons1[16],
     buttons2[16]]
]
keyboard18: list[list[KeyboardButton]] = [
    [buttons1[17],
     buttons2[17]]
]
keyboard19: list[list[KeyboardButton]] = [
    [buttons1[18],
     buttons2[18]]
]
keyboard20: list[list[KeyboardButton]] = [
    [buttons1[19],
     buttons2[19]]
]

my_keyboard1 = ReplyKeyboardMarkup(
    keyboard=keyboard1,
    resize_keyboard=True
)
my_keyboard2 = ReplyKeyboardMarkup(
    keyboard=keyboard2,
    resize_keyboard=True
)
my_keyboard3 = ReplyKeyboardMarkup(
    keyboard=keyboard3,
    resize_keyboard=True
)
my_keyboard4 = ReplyKeyboardMarkup(
    keyboard=keyboard4,
    resize_keyboard=True
)
my_keyboard5 = ReplyKeyboardMarkup(
    keyboard=keyboard5,
    resize_keyboard=True
)
my_keyboard6 = ReplyKeyboardMarkup(
    keyboard=keyboard6,
    resize_keyboard=True
)

my_keyboard7 = ReplyKeyboardMarkup(
    keyboard=keyboard7,
    resize_keyboard=True
)
my_keyboard8 = ReplyKeyboardMarkup(
    keyboard=keyboard8,
    resize_keyboard=True
)
my_keyboard9 = ReplyKeyboardMarkup(
    keyboard=keyboard9,
    resize_keyboard=True
)
my_keyboard10 = ReplyKeyboardMarkup(
    keyboard=keyboard10,
    resize_keyboard=True
)
my_keyboard11 = ReplyKeyboardMarkup(
    keyboard=keyboard11,
    resize_keyboard=True
)
my_keyboard12 = ReplyKeyboardMarkup(
    keyboard=keyboard12,
    resize_keyboard=True
)
my_keyboard13 = ReplyKeyboardMarkup(
    keyboard=keyboard13,
    resize_keyboard=True
)
my_keyboard14 = ReplyKeyboardMarkup(
    keyboard=keyboard14,
    resize_keyboard=True
)
my_keyboard15 = ReplyKeyboardMarkup(
    keyboard=keyboard15,
    resize_keyboard=True
)
my_keyboard16 = ReplyKeyboardMarkup(
    keyboard=keyboard16,
    resize_keyboard=True
)
my_keyboard17 = ReplyKeyboardMarkup(
    keyboard=keyboard17,
    resize_keyboard=True
)
my_keyboard18 = ReplyKeyboardMarkup(
    keyboard=keyboard18,
    resize_keyboard=True
)
my_keyboard19 = ReplyKeyboardMarkup(
    keyboard=keyboard19,
    resize_keyboard=True
)
my_keyboard20 = ReplyKeyboardMarkup(
    keyboard=keyboard20,
    resize_keyboard=True
)

