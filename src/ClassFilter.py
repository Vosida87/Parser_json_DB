class Filter:
    """
    Класс для фильтрации вакансий по нужным критериям
    """
    def __init__(self, data):
        self.data = data

    def remove_with_experience(self):
        """
        Убиарет из списка вакансий те, что не требуют опыта
        """
        new_data = []
        for vacancy in self.data:
            if vacancy['experience'] == "Нет опыта" \
                    or vacancy['experience'] == "Без опыта" \
                    or vacancy['experience'] == "Не имеет значения":
                new_data.append(vacancy)
                self.data = new_data
        return self.data

    def only_with_experience(self):
        """
        Убиарет из списка вакансий те, что требуют опыта
        """
        new_data = []
        for vacancy in self.data:
            if vacancy['experience'] == "Нет опыта" \
                    or vacancy['experience'] == "Без опыта" \
                    or vacancy['experience'] == "Не имеет значения":
                continue
            new_data.append(vacancy)
            self.data = new_data
        return self.data

    def only_superjob(self):
        """
        :return: Только вакансии из superjob
        """
        new_data = []
        for vacancy in self.data:
            if vacancy['website'] == "SuperJob":
                new_data.append(vacancy)
                self.data = new_data
        return self.data

    def only_headhunter(self):
        """
        :return: Только вакансии из headhunter
        """
        new_data = []
        for vacancy in self.data:
            if vacancy['website'] == "HeadHunter":
                new_data.append(vacancy)
                self.data = new_data
        return self.data
