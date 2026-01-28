from cfg import HeroValues, HeroKeys, CM_IN_METER


class BaseEndpoint:

    def __init__(self):
        self.response = None
        self.response_json = None

    @staticmethod
    def _meter_to_cm(hero: dict) -> float:
        """
        :param hero: Герой
        :return: Число сантиметров
        """

        height = hero[HeroKeys.APPEARANCE][HeroKeys.HEIGHT][1].split(' ')
        unit = CM_IN_METER if height[1] == HeroValues.HERO_METERS else 1
        return unit * float(height[0])
