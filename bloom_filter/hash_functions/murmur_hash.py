import mmh3
from .hash_function import HashFunction

# MurMurHash function (TODO: figure out how it works in detail?)

class MurmurHash(HashFunction):
    def hash(self, value, seed):
        return mmh3.hash(value, seed)