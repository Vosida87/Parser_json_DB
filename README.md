# Parser_json_DB

Программа собирает вакансии с HeadHunter и SuperJob по ключевому слову, которое введёт пользователь
Принцип реализации следующий:
Ключевое слово используется при инициализации классов HeadHunterAPI и SuperJobAPI и они получают ответ
Длее идёт форматирование полученных вакансий под один вид, чтобы прогнать их под класс Vacancy
Все полученные данные сохраняются в json файле vacancies
После этого по усмотрению пользователя можно фильтровать их через класс Filter
