from abstract_class import FileWorker
import json
import os


class JsonWorker(FileWorker):
    """
    Класс, для работы с json данными по вакансиям
    """
    def __init__(self, data, path):
        self.data = data
        self.path = path

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.data}', {int(self.path)})"

    def add_vacancies(self):
        """
        добавляет в файл список вакансий
        """
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def get_vacancies(self):
        """
        :return: из файла данные по вакансиям
        """
        with open(self.path, encoding='utf-8') as f:
            data = json.load(f)
        return data

    def remove_vacancies(self):
        """
        удаляет данные по вакансиям
        """
        if os.path.exists(self.path):
            os.remove(self.path)
