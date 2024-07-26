import pytest
from bloom_filter.hash_functions.jenkins_one_at_a_time_hash import JenkinsOneAtATimeHash

@pytest.fixture
def jenkins_hash():
    return JenkinsOneAtATimeHash()

def test_hash(jenkins_hash):
    assert isinstance(jenkins_hash.hash("test_string"), int)
