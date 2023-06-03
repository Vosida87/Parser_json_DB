from src.HeadHunterAPI import HeadHunterAPI
from src.SuperJobAPI import SuperJobAPI
from src.Vacancy import Vacancy


def main():

    sj = SuperJobAPI("Python")
    get_sj = sj.get_request()
    vacancies_sj = sj.formate_info()

    hh = HeadHunterAPI("Python")
    get_hh = hh.get_request()
    vacancies_hh = hh.formate_info()

    all_vacancies = vacancies_hh + vacancies_sj
    for vacancy in all_vacancies:
        i = Vacancy(vacancy)
        print(i.data)
        print('-'*75)


if __name__ == "__main__":
    main()
