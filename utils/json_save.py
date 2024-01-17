import json


class JSONSaver:
    """
    Класс для сохранения вакансий в JSON файл
    """

    def __init__(self):
        """
        Инициализация класса JSONSaver
        """
        self.directory = 'vacancies.json'
        self.data = []

    def add_vacancy(self, vac_list):
        """
        Функция добавляет лист с вакансиями в JSON файл
        :param vac_list: Лист вакансий
        :return None:
        """
        pass

    def delete_by_id(self, vacancy_id):
        """
        Удаляет вакансию из файла JSON по её ID
        :param vacancy_id: ID вакансии
        :return None:
        """
        pass

    def find_by_salary(self, salary):
        """
        Выполняет поиск по файлу JSON с целью найти подходящие по зарплате вакансии
        :param salary: Необходимая зарплата
        :return None:
        """
        pass
