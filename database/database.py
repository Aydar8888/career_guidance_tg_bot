# Шаблон данных для каждого пользователя
user_dict_template = {
    'state': False,
    'question_number': 1,
    'selected_test': None,
    'answers': {
        'test1': [],  # Список ответов для теста 1
        'test2': []   # Список ответов для теста 2
        # Добавьте дополнительные тесты, если они появятся
    }
}

# База данных пользователей
users_db = {}