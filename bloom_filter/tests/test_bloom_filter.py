import pytest
from bloom_filter.bloom_filter import BloomFilter
from bloom_filter.hash_functions.md5_hash import MD5Hash
from bloom_filter.hash_functions.murmur_hash import MurmurHash

@pytest.fixture
def bloom():
    return BloomFilter(100, 3, [MD5Hash(), MurmurHash()])

def test_add(bloom):
    bloom.add_item("im_adding_this_one")
    assert bloom.check_for_item("im_adding_this_one")

def test_contains(bloom):
    bloom.add_item("im_adding_this_one")
    assert bloom.check_for_item("im_adding_this_one")
    assert not bloom.check_for_item("but_not_this_one!")
    