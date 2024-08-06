import json
import os
from matplotlib import pyplot as plt
from bloom_filter.bloom_filter import BloomFilter
import time
import numpy as np

from bloom_filter.hash_functions.murmur_hash import MurmurHash
from bloom_filter.hash_functions.city_hash import CityHash
from data.data_generator import get_natural_language_words, get_random_strings, get_dna_sequences, get_urls

def benchmark(words, bf_bit_capacity, bf_word_capacity, bf_hash_functions):
    # print(f"Benchmarking with {bf_bit_capacity}, {bf_word_capacity}, {bf_hash_functions}")
    
    # Set up the Bloom filter, hash table and Cuckoo filter with the given parameters
    bloom_filter = BloomFilter(bf_bit_capacity, bf_word_capacity, bf_hash_functions)
    hash_table = set()
    python_dynamic_list = []

    # Benchmark add/insert
    bloom_insert_timings = []
    hashset_insert_timings = []
    list_insert_timings = []

    for word in words:
        start_time_bf = time.time()
        bloom_filter.add_item(word)
        delta_time_bf = time.time() - start_time_bf
        bloom_insert_timings.append(delta_time_bf)

        start_time_hashset = time.time()
        hash_table.add(word)
        delta_time_hashset = time.time() - start_time_hashset
        hashset_insert_timings.append(delta_time_hashset)

        start_time_list = time.time()
        python_dynamic_list.append(word)
        delta_time_list = time.time() - start_time_list
        list_insert_timings.append(delta_time_list)

    # Benchmark search
    bloom_search_timings = []
    hashset_search_timings = []
    list_search_timings = []

    for word in words:
        start_time_bf = time.time()
        bloom_filter.add_item(word)
        delta_time_bf = time.time() - start_time_bf
        bloom_search_timings.append(delta_time_bf)

        start_time_hashset = time.time()
        word in hash_table
        delta_time_hashset = time.time() - start_time_hashset
        hashset_search_timings.append(delta_time_hashset)

        start_time_list = time.time()
        word in python_dynamic_list
        delta_time_list = time.time() - start_time_list
        list_search_timings.append(delta_time_list)

    return (bloom_insert_timings, hashset_insert_timings, list_insert_timings, bloom_search_timings, hashset_search_timings, list_search_timings)

def plot_benchmark_results(results, total_number_of_words):
    bloom_insert, hashset_insert, list_insert, bloom_search, hashset_search, list_search = results
    # Change number of bins if necessary
    number_of_bins = 20
    
    x = np.linspace(1, total_number_of_words, number_of_bins)
    def aggregate(data, number_of_bins):
        return np.array_split(data, number_of_bins)

    agg_bloom_insert = [np.mean(bin) for bin in np.array_split(bloom_insert, number_of_bins)]
    agg_hashset_insert = [np.mean(bin) for bin in np.array_split(hashset_insert, number_of_bins)]
    agg_list_insert = [np.mean(bin) for bin in np.array_split(list_insert, number_of_bins)]
    agg_bloom_search = [np.mean(bin) for bin in np.array_split(bloom_search, number_of_bins)]
    agg_hashset_search = [np.mean(bin) for bin in np.array_split(hashset_search, number_of_bins)]
    agg_list_search = [np.mean(bin) for bin in np.array_split(list_search, number_of_bins)]

    plt.figure(figsize=(12, 6))

    # Plot insertion
    plt.subplot(1, 2, 1)
    plt.plot(x, agg_bloom_insert, label='Bloom Filter')
    plt.plot(x, agg_hashset_insert, label='Hashset')
    plt.plot(x, agg_list_insert, label='Dynamic Python List')
    plt.title('Aggregated Insertion Time')
    plt.xlabel('Number of Words (binned)')
    plt.ylabel('Time (seconds)')
    plt.legend()

    # Plot search
    plt.subplot(1, 2, 2)
    plt.plot(x, agg_bloom_search, label='Bloom Filter')
    plt.plot(x, agg_hashset_search, label='Hashset')
    plt.plot(x, agg_list_search, label='Dynamic Python List')
    plt.title('Aggregated Search Time')
    plt.xlabel('Number of Words (binned)')
    plt.ylabel('Time (seconds)')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Set benchmarking parameters here
    bit_capacity = 10 ** 4
    number_of_words_by_design = 10 ** 4
    actual_number_of_words = 10 ** 5
    hash_fns = [MurmurHash(), CityHash()]

    # Get words from data sources
    data_providers = [get_natural_language_words, get_random_strings, get_dna_sequences, get_urls]

    all_results = []
    # Benchmark for each data source
    for data_provider in data_providers:
        results = benchmark(data_provider(actual_number_of_words), bit_capacity, number_of_words_by_design, hash_fns)
        all_results.append(results)
        plot_benchmark_results(results, actual_number_of_words)

    os.makedirs("results", exist_ok=True)
    with open("results/benchmark_results_actual_10_5.json", "w") as file:
        json.dump(all_results, file, indent=4)
