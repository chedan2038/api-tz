import requests

from cfg import BASE_LINK, HeroValues, HeroKeys
from endpoints.base_endpoint import BaseEndpoint


class SuperHero(BaseEndpoint):

    def get_all_heroes(self):
        self.response = requests.get(BASE_LINK + '/all.json')
        self.response_json = self.response.json()

    def get_highest_hero_by_gender_and_job(self, gender: str, job_status: bool) -> dict:
        """
        :param gender: 'Male' | 'Female'
        :param job_status: Отсутствие/наличие работы
        :return: Словарь с самым высоким героем указанного пола и статуса работы
        """

        self.get_all_heroes()
        return max([hero for hero in self.response_json if
                    hero[HeroKeys.APPEARANCE][HeroKeys.GENDER] == gender and (
                            hero[HeroKeys.WORK][HeroKeys.OCCUPATION] != HeroValues.JOB_MISSING) == job_status],
                   key=lambda hero: self._meter_to_cm(hero))
