def make_vacancies_list(hh_vacancies, superjob_vacancies):
    vacancies_list = []
    vacancy_id = 0
    for vacancy in hh_vacancies['items']:
        vacancy_id += 1
        if vacancy['salary'] is None:
            vacancies_list.append([vacancy_id, vacancy['name'], -1, vacancy['alternate_url']])
        else:
            if vacancy['salary']['to'] is not None:
                vacancies_list.append([vacancy_id, vacancy['name'], vacancy['salary']['to'], vacancy['alternate_url']])
            else:
                vacancies_list.append([vacancy_id, vacancy['name'], vacancy['salary']['from'], vacancy['alternate_url']])
    for vacancy in superjob_vacancies['objects']:
        vacancy_id += 1
        if int(vacancy['payment_from']) == 0 and int(vacancy['payment_to']) == 0:
            vacancies_list.append([vacancy_id, vacancy['profession'], -1, vacancy['link']])
        elif int(vacancy['payment_from']) > int(vacancy['payment_to']) == 0:
            vacancies_list.append([vacancy_id, vacancy['profession'], vacancy['payment_from'], vacancy['link']])
        else:
            vacancies_list.append([vacancy_id, vacancy['profession'], vacancy['payment_to'], vacancy['link']])
        return vacancies_list
