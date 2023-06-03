from src.HeadHunterAPI import HeadHunterAPI
from src.SuperJobAPI import SuperJobAPI
from src.Vacancy import Vacancy
from src.ClassFilter import Filter
from src.JsonWorker_class import JsonWorker


def main():

    path = r'../src/vacancies.json'

    print("Введите ключевое слово для поиска вакансий:")
    user_word = input()

    sj = SuperJobAPI(user_word)
    sj.get_request()
    vacancies_sj = sj.formate_info()

    hh = HeadHunterAPI(user_word)
    hh.get_request()
    vacancies_hh = hh.formate_info()

    all_vacancies = vacancies_hh + vacancies_sj

    for vacancy in all_vacancies:
        i = Vacancy(vacancy)
    data = Vacancy.all

    json_file = JsonWorker(data, path)
    json_file.add_vacancies()
    data = json_file.get_vacancies()
    data = Filter(data)

    print("Выберите сайт:\n1.SuperJob\n2. HeadHunter\n3. Сразу оба")
    user_website = int(input())
    print("Выберите вакансии:\n1. С опытом\n2. Без опыта\n3. Без разницы")
    user_mode = int(input())

    if user_website == 3 and user_mode == 3:
        data = data
    elif user_website == 3 and user_mode == 2:
        data.remove_with_experience()
    elif user_website == 3 and user_mode == 1:
        data.only_with_experience()
    elif user_website == 2 and user_mode == 3:
        data.only_headhunter()
    elif user_website == 2 and user_mode == 2:
        data.only_headhunter()
        data.remove_with_experience()
    elif user_website == 2 and user_mode == 1:
        data.only_headhunter()
        data.only_with_experience()
    elif user_website == 1 and user_mode == 3:
        data.only_superjob()
    elif user_website == 1 and user_mode == 2:
        data.only_superjob()
        data.remove_with_experience()
    elif user_website == 1 and user_mode == 1:
        data.only_superjob()
        data.only_with_experience()
    else:
        print("Введены неверные значения")

    empty_list = []
    if data.data == empty_list:
        print('-' * 100)
        print("По вашему запросу ничего не было найдено")
        print('-' * 100)

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
