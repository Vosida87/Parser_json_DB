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


class JsonCreator(ABC):
    pass
