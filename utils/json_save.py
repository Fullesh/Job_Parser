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

    def __repr__(self):
        return f'Класс для работы с JSON файлом. Директория с JSON файлом: {self.directory}\n' \
               f'Данные содержащиеся в JSON в данный момент: {self.data}'

    def add_vacancy(self, vac_list):
        """
        Функция добавляет лист с вакансиями в JSON файл
        :param vac_list: Лист вакансий
        :return None:
        """
        for vac_info in vac_list:
            self.data.append({'id': vac_info[0], 'vacancy_name': vac_info[1], 'vacancy_salary': vac_info[2],
                              'vacancy_url': vac_info[3]})
        with open(self.directory, 'w', encoding='UTF-8') as out_file:
            json.dump(self.data, out_file, indent=4, ensure_ascii=False)

    def delete_by_id(self, vacancy_id):
        """
        Удаляет вакансию из файла JSON по её ID
        :param vacancy_id: ID вакансии
        :return None:
        """
        with open(self.directory, 'r', encoding='UTF-8') as open_file:
            data = json.load(open_file)
        for vac in data:
            if str(vacancy_id) == str(vac['id']):
                print('Got It!')
                del data[vacancy_id-1]
        with open(self.directory, 'w', encoding='UTF-8') as out_file:
            json.dump(data, out_file, indent=4, ensure_ascii=False)
        print(f'Вакансия с ID {vacancy_id} успешно удалена! Файл перезаписан.')

    def find_by_salary(self, salary):
        """
        Выполняет поиск по файлу JSON с целью найти подходящие по зарплате вакансии
        :param salary: Необходимая зарплата
        :return None:
        """
        with open(self.directory, 'r', encoding='UTF-8') as open_file:
            data = json.load(open_file)
        for vac in data:
            if str(salary) == str(vac['vacancy_salary']):
                print(f'_______________________\n'
                      f'ID вакансии: {vac["id"]}\n'
                      f'Название вакансии: {vac["vacancy_name"]}\n'
                      f'Зарплата (от): {vac["vacancy_salary"]}\n'
                      f'Ссылка на вакансию: {vac["vacancy_url"]}\n'
                      f'_______________________')
