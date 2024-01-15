from api_parser.abstract_parser import APIparser
import os
import requests as rq


class HeadHunterParser(APIparser):
    """
    Класс для парсинга вакансий с платформы HeadHunter
    """

    def get_vacancies(self, request):
        """
        Метод для получения вакансий с платформы HeadHunter.
        Возвращает ответ в формате JSON
        """
        params = dict(text=request)
        response = rq.get('https://api.hh.ru/vacancies', params=params)
        return response.json()
