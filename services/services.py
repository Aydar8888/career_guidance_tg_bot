

from lexicon.lexicon_ru import LEXICON_RU
from database.database import users_db
from lexicon.questions import all_tests
from typing import List

# Функция для подсчета результатов теста
def calculate_results(user_id: int) -> List[str]:
    user_data = users_db.get(user_id)
    if not user_data or not user_data['state']:
        return ["Ошибка: пользователь не начал тест."]

    selected_test = user_data['selected_test']
    answers = user_data['answers'][selected_test]

    # Проверяем, что пользователь закончил тест
    if len(answers) != len(all_tests[selected_test]):
        return ["Ошибка: тест не завершен."]

    # Подсчитываем результаты
    results = {
        'test1': {"a": 0, "b": 0},
        'test2': {"a": 0, "b": 0}
    }

    for idx, answer in enumerate(answers, start=1):
        if answer.endswith("а"):
            results[selected_test]["a"] += 1
        elif answer.endswith("б"):
            results[selected_test]["b"] += 1

    # Примерное распределение профессий на основе результатов теста
    recommendations = []
    if selected_test == "Тест Климова (ДДО) 🐾":
        if results["test1"]["a"] > results["test1"]["b"]:
            recommendations.append("Вам подойдут профессии, связанные с уходом за животными и природой (зоолог, ветеринар, агроном).")
        else:
            recommendations.append("Вам подойдут профессии, связанные с техникой и механикой (инженер, механик, автомеханик).")

    elif selected_test == "Тест 2 🧩":
        if results["test2"]["a"] > results["test2"]["b"]:
            recommendations.append("Вам подойдут профессии, связанные с общением и взаимодействием с людьми (менеджер, маркетолог, HR).")
        else:
            recommendations.append("Вам подойдут профессии, связанные с точными науками и техническими задачами (программист, аналитик, математик).")

    return recommendations


# Функция для вывода результата пользователю
def send_result(user_id: int):
    recommendations = calculate_results(user_id)

    if recommendations:
        user_data = users_db[user_id]
        selected_test = user_data['selected_test']
        message = "\n".join(recommendations)

        # Отправляем сообщение пользователю
        return message
    else:
        return "Не удалось подсчитать результат."


