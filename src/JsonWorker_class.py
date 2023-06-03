from abstract_class import FileWorker
import json
import os


class JsonWorker(FileWorker):
    def __init__(self, data, path):
        self.data = data
        self.path = path

    def add_vacancies(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def get_vacancies(self):
        with open(self.path, encoding='utf-8') as f:
            data = json.load(f)
        return data

    def remove_vacancies(self):
        if os.path.exists(self.path):
            os.remove(self.path)
