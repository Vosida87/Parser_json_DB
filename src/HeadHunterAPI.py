from abstract_class import JobCollector
import requests
import json


class HeadHunterAPI(JobCollector):
    def __init__(self, query_word):
        self.query_word = query_word
        self.url = "https://api.hh.ru/vacancies"
        self.params = {"found": 1,
                       "per_page": 50,
                       "pages": 1,
                       "page": 0,
                       "text": self.query_word,
                       "items": [{}]
                       }
        self.headers = {"User-Agent": "MyApp 1.0"}

    def get_request(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.json()['items']
