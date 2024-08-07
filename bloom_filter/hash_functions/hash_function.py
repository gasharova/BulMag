from abc import ABC, abstractmethod

# Base class for the hash functions that we will use
class HashFunction(ABC):
    @abstractmethod
    def hash(self, value, seed):
        # This will be implemented in the concrete classes
        pass

    @abstractmethod
    def __str__(self):
        pass
    
    def __repr__(self):
        pass