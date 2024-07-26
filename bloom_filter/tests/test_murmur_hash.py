import pytest
from bloom_filter.hash_functions.murmur_hash import MurmurHash

@pytest.fixture
def murmur_hash():
    return MurmurHash()

def test_hash(murmur_hash):
    assert isinstance(murmur_hash.hash("test_string"), int)
