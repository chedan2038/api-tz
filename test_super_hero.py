import pytest

from endpoints.super_hero import SuperHero


@pytest.mark.parametrize('gender, job_status', [
    ('Male', True),
    ('Female', True),
    ('Male', False),
    ('Female', False)])
def test_highest_hero_by_gender_and_job(gender, job_status):
    s = SuperHero()

    result = s.get_highest_hero_by_gender_and_job(gender, job_status)
    assert result['appearance']['gender'] == gender
    assert (result['work']['occupation'] != '-') is job_status
