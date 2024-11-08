from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Клавиатура "Да" / "Нет" для вопроса о начале теста
yes_no_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да")],
        [KeyboardButton(text="Нет")]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)

# Клавиатура для выбора теста (например, тест 1 и тест 2)
test_choice_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Тест 1")],
        [KeyboardButton(text="Тест 2")]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)

# Функция для создания клавиатуры с вариантами ответа для вопросов
def create_question_kb(options):
    """
    Создает обычную клавиатуру для вопросов теста.
    :param options: список из двух вариантов ответа (например, ["Вариант 1", "Вариант 2"])
    :return: объект ReplyKeyboardMarkup с двумя кнопками
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=options[0])],
            [KeyboardButton(text=options[1])]
        ],
        resize_keyboard=True, 
        one_time_keyboard=True
    )
    return keyboard

# Клавиатура для возврата в главное меню после завершения теста
game_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Выбрать другой тест")],
        [KeyboardButton(text="Завершить")]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)