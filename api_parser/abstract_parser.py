from abc import ABC, abstractmethod


class APIparser(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями
    """

    def __repr__(self):
        return 'Абстрактный класс для парсинга вакансий. Использует метод get_vacancies'

    @abstractmethod
    def get_vacancies(self, request):
        """
        Метод получающий вакансии с платформы
        """
        pass
