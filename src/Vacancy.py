class Vacancy:

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
