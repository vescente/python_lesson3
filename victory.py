import random

# Список известных людей и их даты рождения
people = {
    "Альберт Эйнштейн": "14.03.1879",
    "Исаак Ньютон": "04.01.1643",
    "Галилео Галилей": "15.02.1564",
    "Мари Кюри": "07.11.1867",
    "Чарльз Дарвин": "12.02.1809",
    "Леонардо да Винчи": "15.04.1452",
    "Никола Тесла": "10.07.1856",
    "Луи Пастер": "27.12.1822",
    "Михаил Ломоносов": "19.11.1711",
    "Георгий Жуков": "01.12.1896"
}

# Функция для преобразования даты в текстовый формат


def date_to_text(date):
    months = {
        "01": "января",
        "02": "февраля",
        "03": "марта",
        "04": "апреля",
        "05": "мая",
        "06": "июня",
        "07": "июля",
        "08": "августа",
        "09": "сентября",
        "10": "октября",
        "11": "ноября",
        "12": "декабря"
    }
    day, month, year = date.split(".")
    return f"{int(day)} {months[month]} {year} года"


def quiz():
    # Выбираем 5 случайных людей
    selected_people = random.sample(list(people.items()), 5)
    correct_answers = 0

    for person, birthdate in selected_people:
        print(f"Введите дату рождения {person} (в формате 'dd.mm.yyyy'):")
        answer = input()
        if answer == birthdate:
            print("Верно!")
            correct_answers += 1
        else:
            print(f"Неверно. Правильный ответ: {date_to_text(birthdate)}")

    print(f"Количество правильных ответов: {correct_answers}")
    print(f"Количество неправильных ответов: {5 - correct_answers}")


if __name__ == "__main__":
    while True:
        quiz()
        again = input("Хотите начать сначала? (да/нет): ")
        if again.lower() != "да":
            break
