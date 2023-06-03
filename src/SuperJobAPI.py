from abstract_class import JobCollector
import requests
import json

class SuperJob(JobCollector):
    def __init__(self, query_word):
        self.query_word = query_word
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.params = {"count": 1,
                       "keyword": self.query_word,
                       }
        self.headers = {"X-Api-App-Id": "v3.r.131154844.742728edb5e885278370f9864ac7066bd528c8c4.0c9796d081133d28c763dc0c7bf9742a3f645bc4"}
        self.vacancies = []

    def get_request(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        json_response = response.json()['objects']
        # json_info = json.dumps(json_response, indent=2, ensure_ascii=False)
        for vacancy in json_response:
            self.vacancies.append(vacancy)
        return json_response

    def formate_info(self):
        for vacancy in self.vacancies:
            formated_vacancy = {
                'name': vacancy['profession'],
                'url': vacancy['link'],
                'description': {'requirement': vacancy['candidat']},

            }


sj = SuperJob("Python")
sj.get_request()
print(sj.vacancies)
