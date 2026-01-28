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

        height = hero['appearance']['height'][1].split(' ')
        unit = 1000 if height[1] == 'meters' else 1
        return unit * float(height[0])
