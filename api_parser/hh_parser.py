from api_parser.abstract_parser import APIparser
import os
import requests as rq


class HeadHunterParser(APIparser):
    """
    ����� ��� �������� �������� � ��������� HeadHunter
    """

    def get_vacancies(self, request):
        """
        ����� ��� ��������� �������� � ��������� HeadHunter.
        ���������� ����� � ������� JSON
        """
        params = dict(text=request)
        response = rq.get('https://api.hh.ru/vacancies', params=params)
        return response.json()
