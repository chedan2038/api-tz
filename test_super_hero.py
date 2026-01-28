import pytest

from cfg import HeroValues, HeroKeys
from endpoints.super_hero import SuperHero


@pytest.mark.parametrize('gender, job_status', [
    (HeroValues.GENDER_M, True),
    (HeroValues.GENDER_F, True),
    (HeroValues.GENDER_M, False),
    (HeroValues.GENDER_F, False)])
def test_highest_hero_by_gender_and_job(gender, job_status):
    s = SuperHero()

    result = s.get_highest_hero_by_gender_and_job(gender, job_status)
    assert result[HeroKeys.APPEARANCE][HeroKeys.GENDER] == gender, 'Не совпадает пол'
    assert (result[HeroKeys.WORK][HeroKeys.OCCUPATION] != HeroValues.JOB_MISSING) is job_status, 'Не совпадает работа'
