from abstract_class import JobCollector
import requests
import json


class HeadHunterAPI(JobCollector):
    def __init__(self, query_word):
        self.query_word = query_word
        self.url = "https://api.hh.ru/vacancies"
        self.params = {"per_page": 1,
                       "text": self.query_word,
                       }
        self.headers = {"User-Agent": "MyApp 1.0"}
        self.vacancies = []

    def get_request(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        json_response = response.json()['items']
        # json_info = json.dumps(json_response, indent=2, ensure_ascii=False)
        for vacancy in json_response:
            self.vacancies.append(vacancy)
        return json_response


hh = HeadHunterAPI("Python")
hh.get_request()
print(hh.vacancies)