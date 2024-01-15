from api_parser.abstract_parser import APIparser
import os
import requests as rq


class SuperJobParser(APIparser):
    """
    Класс для парсинга вакансий с платформы SuperJob
    """
    def __init__(self):
        self.sj_key = os.getenv('SJ_KEY')

    def get_vacancies(self, request):
        """
        Метод для получения вакансий с платформы SuperJob.
        Возвращает ответ в формате JSON
        """
        params = dict(keyword=request)
        headers = {"X-Api-App-Id": self.sj_key}
        response = rq.get("https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers)
        return response.json()
