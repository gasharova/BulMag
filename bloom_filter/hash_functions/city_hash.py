import cityhash
from .hash_function import HashFunction

class CityHash(HashFunction):
    def hash(self, value, seed=0):
        return cityhash.CityHash32(value, seed)
