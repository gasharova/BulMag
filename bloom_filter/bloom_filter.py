from bitarray import bitarray
import math

class BloomFilter:
    def __init__(self, bit_array_size, expected_items_number, hash_functions_list):
        # Initialize class members from constructor parameters
        self.__bit_array_size = bit_array_size
        # Not going to use this one but may be accessed for future project improvements
        self.__expected_items_number = expected_items_number
        self.__hash_functions_number = math.ceil((bit_array_size / expected_items_number) * math.log(2))
        # Initialize the bit array with the given size and nullify each bit
        self.__bit_array = bitarray(bit_array_size)
        self.__bit_array.setall(0)
        self.__added_items_number = 0
        # Extract the first k hash functions and set them for our class
        self.__hash_functions = hash_functions_list[:self.__hash_functions_number]

    # Low-level (bit) setters and getters
    def __set_bit__(self, bit_index):
        self.__bit_array[bit_index] = 1
    
    def __get_bit__(self, bit_index):
        return self.__bit_array[bit_index]

    # Printout functions for debugging and quick internal state visualising
    def __str__(self):
        return (f"Bloom filter with length: {self.__bit_array_size}, "
                f"expected number of items: {self.__expected_items_number}, "
                f"current number of items: {self.__added_items_number}, "
                f"hash functions used: {self.__hash_functions}. ")
    
    def __repr__(self):
        return (f"BloomFilter(bit_array_size={self.__bit_array_size}, "
                f"expected_items_number={self.__expected_items_number}, "
                f"added_items_number={self.__added_items_number}, "
                f"hash_functions_number={self.__hash_functions_number}, "
                f"hash_functions={self.__hash_functions})")
    
    # High-level (item) setters and getters
    # Bloom filters do not allow update/delete operations!
    def add_item(self, item):
        for i, hash_function in enumerate(self.__hash_functions):
            # This works because we have a common parent of each hash function, so we just call method hash()
            digest_index = hash_function.hash(item, i) % self.__bit_array_size
            self.__set_bit__(digest_index)
        self.__added_items_number += 1
    
    def check_for_item(self, item):
        for i, hash_function in enumerate(self.__hash_functions):
            # Hash it..
            digest_index = hash_function.hash(item, i) % self.__bit_array_size
            # If this bit is missing, then for sure we have a true negative.
            if not self.__get_bit__(digest_index):
                return False
        # In all other cases, we have a (true/false) positive.
        return True
    
    # Preparing getters for the last 2 requirements
    def get_false_positive_rate(self):
        bit_zero_probability = (1 - 1/self.__bit_array_size) ** (self.__hash_functions_number * self.__added_items_number)
        false_positive_rate = (1 - bit_zero_probability) ** self.__hash_functions_number
        return false_positive_rate

    def get_compression_rate(self):
        compression_rate = (1 - sum(self.__bit_array) / self.__bit_array_size)
        return compression_rate
