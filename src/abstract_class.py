from abc import ABC, abstractmethod


class JobCollector(ABC):
    """
    Абстрактный класс для создания запроса
    """
    @abstractmethod
    def get_request(self):
        """
        :return: request запрос
        """
        pass


class FileWorker(ABC):
    """
    Абстрактный класс, для добавления вакансий в файл,
    считывания вакансий с файла,
    а также удаления файла
    """

    @abstractmethod
    def add_vacancies(self):
        pass


    @abstractmethod
    def get_vacancies(self):
        pass


    @abstractmethod
    def remove_vacancies(self):
        pass
