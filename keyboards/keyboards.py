from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Главное меню с эмодзи
main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Выбрать тест 🎯")],
        [KeyboardButton(text="GitHub 🌐")],
        [KeyboardButton(text="Оставить отзыв ✍️")],
        [KeyboardButton(text="О проекте 📚")]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

# Клавиатура "Да" / "Нет" для вопроса о начале теста с эмодзи
yes_no_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да ✅")],
        [KeyboardButton(text="Нет ❌")]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)

# Клавиатура для выбора теста с эмодзи
test_choice_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Тест Климова (ДДО) 🐾")],
        [KeyboardButton(text="Тест 2 🧩")],
        [KeyboardButton(text="Вернуться в главное меню 🔙")]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)

# Функция для создания клавиатуры с вариантами ответа для вопросов с эмодзи
def create_question_kb(options):
    """
    Создает обычную клавиатуру для вопросов теста с эмодзи.
    :param options: список из двух вариантов ответа (например, ["Вариант 1", "Вариант 2"])
    :return: объект ReplyKeyboardMarkup с двумя кнопками
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=options[0])],
            [KeyboardButton(text=options[1])],
            [KeyboardButton(text="Вернуться в главное меню 🔙")]
        ],
        resize_keyboard=True, 
        one_time_keyboard=True
    )
    return keyboard

# Клавиатура для возврата в главное меню после завершения теста с эмодзи
game_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Выбрать другой тест 🎯")],
        [KeyboardButton(text="Завершить 🚪")]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)
