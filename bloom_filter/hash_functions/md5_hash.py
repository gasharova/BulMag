import hashlib
from .hash_function import HashFunction

# Standard MD5 hashing

class MD5Hash(HashFunction):
    def hash(self, value, seed):
        return int(hashlib.md5((str(seed) + value).encode()).hexdigest(), 16)