import pytest
from bloom_filter.hash_functions.sha256_hash import Sha256Hash

@pytest.fixture
def sha256_hash():
    return Sha256Hash()

def test_hash(sha256_hash):
    assert isinstance(sha256_hash.hash("test_string"), int)
