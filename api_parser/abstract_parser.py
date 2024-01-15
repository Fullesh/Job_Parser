from abc import ABC, abstractmethod


class APIparser(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями
    """
    @abstractmethod
    def get_vacancies(self, request):
        """
        Метод получающий вакансии с платформы
        """
        pass
