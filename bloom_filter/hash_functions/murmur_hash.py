import mmh3
from .hash_function import HashFunction

# MurMurHash

class MurmurHash(HashFunction):
    def hash(self, value, seed=0):
        return mmh3.hash(value, seed)

    def __str__(self):
        return "MurmurHash"
    
    def __repr__(self):
        return "MurmurHash()"
