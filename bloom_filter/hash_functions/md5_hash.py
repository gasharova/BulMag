import hashlib
from .hash_function import HashFunction

# Standard MD5 hashing
# TODO - is it too slow?

class MD5Hash(HashFunction):
    def hash(self, value, seed=0):
        return int(hashlib.md5((str(seed) + value).encode()).hexdigest(), 16)
    
    def __str__(self):
        return "MD5Hash"
    
    def __repr__(self):
        return "MD5Hash()"
