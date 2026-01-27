import requests

from cfg import BASE_LINK
from endpoints.base_endpoint import BaseEndpoint


class SuperHero(BaseEndpoint):

    def get_all_heroes(self):
        self.response = requests.get(BASE_LINK + '/all.json')
        self.response_json = self.response.json()

    def get_highest_hero_by_gender_and_job(self, gender: str, job_status: bool) -> dict:
        """
        :param gender: 'Male' | 'Female'
        :param job_status:
        :return: Словарь с самым высоким героем указанного пола и статуса работы
        """

        self.get_all_heroes()
        return max([i for i in self.response_json if
                    i['appearance']['gender'] == gender and (i['work']['occupation'] != '-') == job_status],
                   key=lambda x: self._meter_to_cm(x))
