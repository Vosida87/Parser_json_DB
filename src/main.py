from src.HeadHunterAPI import HeadHunterAPI
from src.SuperJobAPI import SuperJobAPI
from src.Vacancy import Vacancy
from src.ClassFilter import Filter
from src.JsonWorker_class import JsonWorker


def main():
    """
    Основная программа для пользователя
    """

    # задаём путь куда будут сохраняться данные о вакансиях

    path = r'../src/vacancies.json'

    print("Введите ключевое слово для поиска вакансий:")
    user_word = input()

    # Получем ответ от SuperJob и HeadHunter о вакансиях

    sj = SuperJobAPI(user_word)
    sj.get_request()
    vacancies_sj = sj.formate_info()

    hh = HeadHunterAPI(user_word)
    hh.get_request()
    vacancies_hh = hh.formate_info()

    # Соединяем все вакансии в один список

    all_vacancies = vacancies_hh + vacancies_sj

    for vacancy in all_vacancies:
        i = Vacancy(vacancy)
    data = Vacancy.all

    json_file = JsonWorker(data, path)
    json_file.add_vacancies()
    data = json_file.get_vacancies()

    # Создаём экземпляр класса Filter для дальнейшей фильтрации данных
    # в зависимости от выбора пользователя

    data = Filter(data)

    print("Выберите сайт:\n1.SuperJob\n2. HeadHunter\n3. Сразу оба")
    user_website = int(input())
    print("Выберите вакансии:\n1. С опытом\n2. Без опыта\n3. Без разницы")
    user_mode = int(input())

    # Варианты фильтрации в зависимости от предпочтений пользователя

    if user_mode == 2:
        data.remove_with_experience()
    elif user_mode == 1:
        data.only_with_experience()

    if user_website == 2:
        data.only_headhunter()
    elif user_website == 1:
        data.only_superjob()

    if user_mode != 1 or user_mode != 2 or user_mode != 3:
        print("Введены неверные значения")
    if user_website != 1 or user_website != 2 or user_website != 3:
        print("Введены неверные значения")

    # На случай если было введено неккоректно ключевое слово

    empty_list = []
    if data.data == empty_list:
        print('-' * 100)
        print("По вашему запросу ничего не было найдено")
        print('-' * 100)

    # Далее перебор отфильтрованных вакансий с отображением нужных данных пользователю

    for vacancy in data.data:
        print(f"Сайт: {vacancy['website']}")
        print(f"Вакансия: {vacancy['name']}")
        print(f"Адрес: {vacancy['url']}")
        print(f"Опыт: {vacancy['experience']}")
        if vacancy['payment_from'] is None \
                or vacancy['payment_from'] == '0' \
                or vacancy['payment_from'] == 0:
            print(f"З/п от: Не указана")
        else:
            print(f"З/п от: {vacancy['payment_from']} {vacancy['currency']}")
        if vacancy['payment_to'] is None \
                or vacancy['payment_to'] == '0' \
                or vacancy['payment_to'] == 0:
            print(f"З/п до: Не указана")
        else:
            print(f"З/п до: {vacancy['payment_to']} {vacancy['currency']}")
        print('-'*100)


if __name__ == "__main__":
    main()
