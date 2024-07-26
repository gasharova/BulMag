import hashlib
from .hash_function import HashFunction

class Sha256Hash(HashFunction):
    def hash(self, value, seed=0):
        value = value.encode('utf-8') if isinstance(value, str) else value
        value = str(seed).encode('utf-8') + value
        return int(hashlib.sha256(value).hexdigest(), 16)
