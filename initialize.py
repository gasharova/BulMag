from bloom_filter.bloom_filter import BloomFilter
from bloom_filter.hash_functions.md5_hash import MD5Hash
from bloom_filter.hash_functions.murmur_hash import MurmurHash

from data.data_generator import get_natural_language_words
from data.data_generator import get_random_strings
from data.data_generator import get_dna_sequences
from data.data_generator import get_urls

md5_hash_function = MD5Hash()
murmur_hash_function = MurmurHash()

only_md5 = [md5_hash_function]
both = [md5_hash_function, murmur_hash_function]

bloom_filter_only_md5 = BloomFilter(bit_array_size=100, expected_items_number=20, hash_functions_list=only_md5)
bloom_filter_both = BloomFilter(bit_array_size=100, expected_items_number=20, hash_functions_list=both)

bloom_filter_only_md5.add_item("someword")
bloom_filter_only_md5.add_item("yetanotherword")
print(bloom_filter_only_md5)
print(bloom_filter_only_md5.check_for_item("someword"))

bloom_filter_both.add_item("johndoe")
bloom_filter_both.add_item("helloworld")
print(bloom_filter_both)
print(bloom_filter_both.check_for_item("johndoe"))
print(bloom_filter_both.check_for_item("nojohndoe"))

print("natural language words")
print(get_natural_language_words(n=20))

print("random strings")
print(get_random_strings(n=20, max_length=10))

print("random strings")
print(get_dna_sequences(n=20))

print("urls")
print(get_urls(n=20))
