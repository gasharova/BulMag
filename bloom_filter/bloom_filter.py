from bitarray import bitarray

class BloomFilter:
    def __init__(self, bit_array_size, hash_functions_list):
        # Initialize class members from constructor parameters
        self.__bit_array_size = bit_array_size
        self.__hash_functions_list = hash_functions_list
        # Initialize the bit array with the given size and nullify each bit
        self.__bit_array = bitarray(bit_array_size)
        self.__bit_array.setall(0)

    # Low-level (bit) setters and getters
    def __set_bit__(self, bit_index):
        self.__bit_array[bit_index] = 1
    
    def __get_bit__(self, bit_index):
        return self.__bit_array[bit_index]
    
    # High-level (item) setters and getters
    def add_item(self, item):
        for i, hash_function in enumerate(self.__hash_functions_list):
            # This works because we have a common parent of each hash function, so we just call method hash()
            digest_index = hash_function.hash(item, i) % self.__bit_array_size
            self.__set_bit__(digest_index)
    
    def check_for_item(self, item):
        for i, hash_function in enumerate(self.__hash_functions_list):
            # Hash it..
            digest_index = hash_function.hash(item, i) % self.__bit_array_size
            # If this bit is missing, then for sure we have a true negative.
            if not self.__get_bit__(digest_index):
                return False
        # In all other cases, we have a (true/false) positive.
        return True
