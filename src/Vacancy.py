class Vacancy:
    def __init__(self, vacancy):
        self.website = vacancy['website']
        self.name = vacancy['name']
        self.url = vacancy['url']
        self.experience = vacancy['experience']
        self.payment_from = vacancy['payment_from']
        self.payment_to = vacancy['payment_to']
        self.currency = vacancy['currency']

        self.data = {'website': self.website,
                     'name': self.name,
                     'url': self.url,
                     'experience': self.experience,
                     'payment_from': self.payment_from,
                     'payment_to': self.payment_to,
                     'currency': self.currency,
                     }
