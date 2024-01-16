def print_top_vacancies(vac_list, top_n):
    """
    ������� ������� �������� ���������� ������� �������� �� ������
    :param vac_list: ������ ����������������� ��������
    :param top_n: ���������� ��������� ������� ��������
    :return None:
    """
    sorted_list = sorted(vac_list, key=lambda x: x[2], reverse=True)
    for i in range(top_n):
        print(sorted_list[i])
