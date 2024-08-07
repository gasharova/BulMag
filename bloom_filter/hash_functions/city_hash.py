import cityhash
from .hash_function import HashFunction

class CityHash(HashFunction):
    def hash(self, value, seed=0):
        return cityhash.CityHash64WithSeed(value, seed)

    def __str__(self):
        return "CityHash"
    
    def __repr__(self):
        return "CityHash()"
