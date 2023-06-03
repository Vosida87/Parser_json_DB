from abstract_class import JobCollector
import requests
import json


class HeadHunterAPI(JobCollector):
    """
    Класс для получения вакансий из superjob по api
    инициализируется по ключевому слову
    """
    def __init__(self, query_word):
        self.query_word = query_word
        self.url = "https://api.hh.ru/vacancies"
        self.params = {"per_page": 25,
                       "text": self.query_word,
                       }
        self.headers = {"User-Agent": "MyApp 1.0"}
        self.vacancies = []

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.query_word}', {int(self.url)}, {self.params})"

    def get_request(self):
        """
        функция запроса, возвращает вакансии
        """
        response = requests.get(self.url, params=self.params, headers=self.headers)
        json_response = response.json()['items']
        for vacancy in json_response:
            self.vacancies.append(vacancy)
        return json_response

    def formate_info(self):
        """
        Форматируем в свой словарь, для дальнейшего объединения с SJ API
        """
        formatted_vacancies = []
        for vacancy in self.vacancies:
            formatted_vacancy = {
                'website': 'HeadHunter',
                'name': vacancy['name'],
                'url': vacancy['alternate_url'],
                'experience': vacancy['experience']['name'],
            }

            # Иногда параметр зарплаты None

            if vacancy['salary'] is not None:
                formatted_vacancy['payment_from'] = vacancy['salary']['from']
                formatted_vacancy['payment_to'] = vacancy['salary']['to']
                formatted_vacancy['currency'] = vacancy['salary']['currency']
            else:
                formatted_vacancy['payment_from'] = None
                formatted_vacancy['payment_to'] = None
                formatted_vacancy['currency'] = None
            formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies
