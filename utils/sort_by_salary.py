def sort_by_salary(vac_list):
    """
    Функция возвращающая отсортированный по зарплате список
    :param vac_list:
    :return:
    """
    sorted_list = sorted(vac_list, key=lambda x: x[2], reverse=True)
    for vac in sorted_list:
        print(*vac)
