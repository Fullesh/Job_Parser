from utils.json_save import *
from utils.sort_by_salary import *
from utils.print_vacancies_list import print_vacancies
from api_parser.sj_parser import SuperJobParser
from api_parser.hh_parser import HeadHunterParser
import os

# Создаём список команд для случаев когда уже есть файл JSON и когда его нет
commands = []
commands_json = []
json_work = 'n'

# Создание экземпляров класса парсеров
hh_instance = HeadHunterParser()
sj_instance = SuperJobParser()

# Проверяем существует ли файл с вакансиями в директории
if os.path.exists('vacancies.json'):
    json_work = input('У вас уже есть файл JSON. Продолжить работу с ним или начнём с нуля?')


def choose_commands(comands, json_or_scratch):
    """
    Метод для выбора команды для исполнения.
    :param comands: Лист комманд для исполнения
    :param json_or_scratch: Проверка работаем ли с файлом JSON или с нуля
    :return None:
    """
    for i in comands:
        print(f'{i+1}. {comands[i]}')
    try:
        command = int(input('\nКоманда для исполнения: '))
        if json_or_scratch in ['y', 'yes', 'lf']:
            execute_json_commands(command)
        else:
            execute_regular_commands(command)
    except ValueError:
        print('Ошибка. Была введена строка!')


# Проверяем работаем ли с готовым файлом JSON. Если нет, то работаем с нуля
if json_work.lower() in ['y', 'yes', 'lf']:
    choose_commands(commands_json, json_work)
else:
    search_query = input('Введите вакансию для поиска: ')
    hh_vacancies = hh_instance.get_vacancies(search_query)
    sj_vacancies = sj_instance.get_vacancies(search_query)
    show_list = input('Вакансии загружены. Вывести лист вакансий? ')
    if show_list in ['y', 'yes', 'lf']:
        print_vacancies(hh_vacancies, sj_vacancies)
    else:
        choose_commands(commands, json_work)
