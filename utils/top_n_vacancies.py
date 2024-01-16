def print_top_vacancies(vac_list, top_n):
    """
    ‘ункци€ выводит заданное количество топовых вакансий из списка
    :param vac_list: —писок неотсортированных вакансий
    :param top_n:  оличество выводимых топовых вакансий
    :return None:
    """
    sorted_list = sorted(vac_list, key=lambda x: x[2], reverse=True)
    for i in range(top_n):
        print(sorted_list[i])
