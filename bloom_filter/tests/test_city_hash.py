import pytest
from bloom_filter.hash_functions.city_hash import CityHash

@pytest.fixture
def city_hash():
    return CityHash()

def test_hash(city_hash):
    assert isinstance(city_hash.hash("test_string"), int)
