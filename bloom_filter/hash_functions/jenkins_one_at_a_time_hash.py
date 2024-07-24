from .hash_function import HashFunction

class JenkinsOneAtATimeHash(HashFunction):
    def hash(self, value, seed=0):
        hash_value = seed
        for char in value:
            hash_value += ord(char)
            hash_value += (hash_value << 10)
            hash_value ^= (hash_value >> 6)
        hash_value += (hash_value << 3)
        hash_value ^= (hash_value >> 11)
        hash_value += (hash_value << 15)
        return hash_value
