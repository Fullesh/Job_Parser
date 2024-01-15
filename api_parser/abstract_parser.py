from abc import ABC, abstractmethod


class APIparser(ABC):
    """
    ����������� ����� ��� ������ � API ������ � ����������
    """
    @abstractmethod
    def get_vacancies(self, request):
        """
        ����� ���������� �������� � ���������
        """
        pass
