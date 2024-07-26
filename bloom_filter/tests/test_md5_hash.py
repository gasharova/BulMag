import pytest
from bloom_filter.hash_functions.md5_hash import MD5Hash

@pytest.fixture
def md5_hash():
    return MD5Hash()

def test_hash(md5_hash):
    assert isinstance(md5_hash.hash("test_string"), int)
