from abc import ABC, abstractmethod


class JobCollector(ABC):
    """
    Абстрактный класс для работы с вакансиями
    """
    @abstractmethod
    def get_request(self):
        """
        :return: request запрос
        """
        pass
