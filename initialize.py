from bloom_filter.bloom_filter import BloomFilter
from bloom_filter.hash_functions.md5_hash import MD5Hash
from bloom_filter.hash_functions.murmur_hash import MurmurHash


# Start script here...

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