from abstract_class import JobCollector
import requests
import json

class SuperJobAPI(JobCollector):
    """
    Класс для получения вакансий из superjob по api
    инициализируется по ключевому слову
    """
    def __init__(self, query_word):
        self.query_word = query_word
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.params = {"count": 25,
                       "keyword": self.query_word,
                       }
        self.__headers = {"X-Api-App-Id": "v3.r.131154844.742728edb5e885278370f9864ac7066bd528c8c4.0c9796d081133d28c763dc0c7bf9742a3f645bc4"}
        self.vacancies = []

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.query_word}', {int(self.url)}, {self.params})"

    @property
    def headers(self):
        return f'{self.__headers}'

    def get_request(self):
        """
        функция запроса, возвращает вакансии
        """
        response = requests.get(self.url, params=self.params, headers=self.__headers)
        json_response = response.json()['objects']
        for vacancy in json_response:
            self.vacancies.append(vacancy)
        return json_response

    def formate_info(self):
        """
        Форматируем в свой словарь, для дальнейшего объединения с HH API
        """
        formatted_vacancies = []
        for vacancy in self.vacancies:
            formatted_vacancy = {
                'website': 'SuperJob',
                'name': vacancy['profession'],
                'url': vacancy['link'],
                'experience': vacancy['experience']['title'],
                'payment_from': vacancy['payment_from'],
                'payment_to': vacancy['payment_to'],
                'currency': vacancy['currency'],
            }
            formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies
