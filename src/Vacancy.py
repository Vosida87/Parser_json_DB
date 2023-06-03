class Vacancy:
    """
    Класс для работы с вакансиями, определяет их основные
    атрибуты и сохраняет созданные экземпляры в all
    """

    all = []

    def __init__(self, vacancy):
        self.website = vacancy['website']
        self.name = vacancy['name']
        self.url = vacancy['url']
        self.experience = vacancy['experience']
        self.payment_from = vacancy['payment_from']
        self.payment_to = vacancy['payment_to']
        self.currency = vacancy['currency']

        Vacancy.all.append(vacancy)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {int(self.website)}, {self.url})"

    def __str__(self):
        return self.name

    # Для сравнения отдельных вакансий можно воспользоваться магическими методами:

    def __sub__(self, other):
        """
        Вычитание
        """
        return int(self.payment_to) - int(other.payment_to)

    def __eq__(self, other):
        """
        Определяет поведение оператора равенства
        """
        if int(self.payment_to) == int(other.payment_to):
            return True
        return False

    def __ne__(self, other):
        """
        Определяет поведение оператора неравенства
        """
        if int(self.payment_to) != int(other.payment_to):
            return True
        return False

    def __lt__(self, other):
        """
        Определяет поведение оператора меньше
        """
        if int(self.payment_to) < int(other.payment_to):
            return True
        return False

    def __gt__(self, other):
        """
        Определяет поведение оператора больше
        """
        if int(self.payment_to) > int(other.payment_to):
            return True
        return False

    def __le__(self, other):
        """
        Определяет поведение оператора меньше или равно
        """
        if int(self.payment_to) <= int(other.payment_to):
            return True
        return False

    def __ge__(self, other):
        """
        Определяет поведение оператора больше или равно
        """
        if int(self.payment_to) >= int(other.payment_to):
            return True
        return False
