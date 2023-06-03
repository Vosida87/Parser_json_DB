from src.HeadHunterAPI import HeadHunterAPI
from src.SuperJobAPI import SuperJobAPI
from src.Vacancy import Vacancy
from src.ClassFilter import Filter
from src.JsonWorker_class import JsonWorker


def main():

    path = r'../src/vacancies.json'

    sj = SuperJobAPI("Python")
    sj.get_request()
    vacancies_sj = sj.formate_info()

    hh = HeadHunterAPI("Python")
    hh.get_request()
    vacancies_hh = hh.formate_info()

    all_vacancies = vacancies_hh + vacancies_sj

    for vacancy in all_vacancies:
        i = Vacancy(vacancy)
    data = Vacancy.all

    json_file = JsonWorker(data, path)
    json_file.add_vacancies()
    json_info = json_file.get_vacancies()

    for vacancy in json_info:
        print(f"Сайт: {vacancy['website']}")
        print(f"Вакансия: {vacancy['name']}")
        print(f"Адрес: {vacancy['url']}")
        print(f"Опыт: {vacancy['experience']}")
        print(f"З/п от: {vacancy['payment_from']} {vacancy['currency']}")
        print(f"З/П до: {vacancy['payment_to']} {vacancy['currency']}")
        print('--'*100)

if __name__ == "__main__":
    main()
