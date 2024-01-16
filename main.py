from utils.json_save import *
from utils.sort_by_salary import *
from utils.top_n_vacancies import print_top_vacancies
from utils.make_vac_list import make_vacancies_list
from api_parser.sj_parser import SuperJobParser
from api_parser.hh_parser import HeadHunterParser
import os

# Создаём список команд для случаев когда уже есть файл JSON и когда его нет
commands = ['Вывести отсортированные по зарплате вакансии', 'Вывести топ вакансий', 'Выход']
commands_json = ['Найти вакансию по id', 'Вывести вакансии по зарплате', 'Удалить вакансию', 'Выход']
json_work = 'n'

# Создание экземпляров класса парсеров
hh_instance = HeadHunterParser()
sj_instance = SuperJobParser()

# Проверяем существует ли файл с вакансиями в директории
if os.path.exists('vacancies.json'):
    json_work = input('У вас уже есть файл JSON. Продолжить работу с ним или начнём с нуля? [y/n]: ')


def choose_commands(comands, json_or_scratch):
    """
    Метод для выбора команды для исполнения.
    :param comands: Лист комманд для исполнения
    :param json_or_scratch: Проверка работаем ли с файлом JSON или с нуля
    :return None:
    """
    for i in range(len(comands)):
        print(f'{i + 1}. {comands[i]}')
    try:
        command = int(input('\nКоманда для исполнения: '))
        if json_or_scratch in ['y', 'yes', 'lf']:
            execute_json_commands(command)
        else:
            execute_regular_commands(command, vacancies_list)
    except ValueError:
        print('Ошибка. Была введена строка!')


def execute_json_commands(command):
    """
    Метод для исполнения команды при существовании файла JSON
    :param command: Команда для исполнения
    :return None:
    """
    pass


def execute_regular_commands(command, vac_list):
    """
    Метод для выполнения команд когда не существует готовый файл JSON
    :param command: Номер команды для исполнения
    :param vac_list: Лист вакансий
    :return None:
    """
    if command == 1:
        print(sort_by_salary(vac_list))
    elif command == 2:
        try:
            top_n = int(input('Введите количество выводимых в топе вакансий: '))
            print_top_vacancies(top_n)
        except ValueError:
            print('Ошибка. Была введена строка!')
    elif command == 3:
        print('Команда принята, выходим...')
        return exit('Выход из приложения')


# Проверяем работаем ли с готовым файлом JSON. Если нет, то работаем с нуля
if json_work.lower() in ['y', 'yes', 'lf']:
    choose_commands(commands_json, json_work)
else:
    search_query = input('Введите вакансию для поиска: ')  # Запрашиваем вакансию для поиска
    hh_vacancies = hh_instance.get_vacancies(search_query)  # Парсим вакансии по запросу
    sj_vacancies = sj_instance.get_vacancies(search_query)  # Парсим вакансии по запросу
    vacancies_list = make_vacancies_list(hh_vacancies, sj_vacancies)
    show_list = input('Вакансии загружены. Вывести лист вакансий? ')  # Спрашиваем нужно ли вывести лист вакансий
    if show_list in ['y', 'yes', 'lf']:  # Если да то выводим вакансии
        for vac in vacancies_list:
            print(*vac)
    else:
        pass
    choose_commands(commands, json_work)
