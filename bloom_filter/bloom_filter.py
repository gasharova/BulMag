from bitarray import bitarray
import math

class BloomFilter:
    def __init__(self, bit_array_size, expected_items_number, hash_functions_list):
        # Initialize class members from constructor parameters
        self.__bit_array_size = bit_array_size
        # Not going to use this one but may be accessed for future project improvements
        self.__expected_items_number = expected_items_number
        self.__hash_functions_number = math.ceil((bit_array_size / expected_items_number) * math.log(2))
        self.__hash_functions_list = hash_functions_list
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
    
    # High-level (item) setters and getters
    # Bloom filters do not allow update/delete operations!
    def add_item(self, item):
        for i, hash_function in enumerate(self.__hash_functions_list):
            # This works because we have a common parent of each hash function, so we just call method hash()
            digest_index = hash_function.hash(item, i) % self.__bit_array_size
            self.__set_bit__(digest_index)
        self.__added_items_number += 1
    
    def check_for_item(self, item):
        for i, hash_function in enumerate(self.__hash_functions_list):
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
        compression_rate = (1 - sum(self.bit_array) / self.__bit_array_size) * 100
        return compression_rate
