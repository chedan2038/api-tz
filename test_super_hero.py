import pytest

from cfg import GENDER_M, GENDER_F, JOB_MISSING
from endpoints.super_hero import SuperHero


@pytest.mark.parametrize('gender, job_status', [
    (GENDER_M, True),
    (GENDER_F, True),
    (GENDER_M, False),
    (GENDER_F, False)])
def test_highest_hero_by_gender_and_job(gender, job_status):
    s = SuperHero()

    result = s.get_highest_hero_by_gender_and_job(gender, job_status)
    assert result['appearance']['gender'] == gender, 'Не совпадает пол'
    assert (result['work']['occupation'] != JOB_MISSING) is job_status, 'Не совпадает работа'
