from abc import ABC, abstractmethod


class JobCollector(ABC):
    """
    Абстрактный класс для получения вакансий
    """
    @abstractmethod
    def get_request(self):
        """
        :return: request запрос
        """
        pass


class FileWorker(ABC):


    @abstractmethod
    def add_vacancies(self):
        pass


    @abstractmethod
    def get_vacancies(self):
        pass


    @abstractmethod
    def remove_vacancies(self):
        pass
