# BulMag
Bloom filter implementation and analysis

Members:
@gasharova @Istvan1996

# Criteria coverage

**1. Version control and contributions tracking**

The code collaboration was done on GitHub. Commit messages followed structural and semantic guidelines for good practices. This READme file was created for more details on directories, setup, and way of working.

**2. Implementation approach**

This Bloom filter was implemented using an _object-oriented_ _(OO)_ approach. This was decided since we were looking at multiple different OO principles: encapsulation (since we don't want to mess with filter internals regarding bit_array, and each filter will have immutable attributes i.e. size due to design), polymorphism/inheritance (for each hash function, we have a common _hash()_ method inherited from the base, so we can hash a key without caring what's the algorithm behind it), abstraction (only functions for adding and checking are public).

Comments are present in the code files for further elaboration.

__ __init__ __.py files were created in the directories to ensure the parser treats them like modules.

Seeding (defaulted to 0) was added to each hash function for reproducibility and extra experimenting. A list of hash functions is passed to the filter class at function definition, allowing for modularity and flexibility by switching between functions we like without changing the internal implementation. Not all functions may be used, but the parameter _k_ is calculated for our filter design, and the _k_ functions are extracted and used.

Since different hash functions of different bit sizes are used, hash length is normalized inside the Bloom Filter.

Each class has implementations of __ __repr__ __ and __ __str__ __ functions as per good programming practices.

**3. Testing the implementation**

Implementation is tested using basic unit tests.
For the hash functions, all of them use external libraries with many contributors and downloads and are maintained and tested by the Python community.
For the filter itself, tests were added for the addition and lookup procedures. 

**4. Testing with different data types**

In order to provide sufficient data for both hash function distribution testing and HPC experiments, four generator/loader functions were added in the *data* directory.
- *get_random_strings* and *get_urls* are generator methods for random strings and URLs. The former randomizes string length and the latter provides a realistic URL structure with depth and queries.
- *get_natural_language_words* and *get_dna_sequences* use a *.txt* and *.csv* dataset (respectively), each available for project usage at the addresses below. Both functions have loading optimizations, and all four data type providers can generate a sample of any size *n*.

https://github.com/dwyl/english-words/blob/master/words_alpha.txt
https://www.kaggle.com/datasets/adnanyaramis/coding-noncoding-dna-sequences

In the Jupyter notebook, tests were written and performed using all 5 hash functions and the 4 data types to see which hashing functions perform better for which kinds of data. Statistical analysis was done by calculating chi-squared, p-value and standard deviation for each data type and hashing algorithm and evaluating the results.

**5. Discussing space and time complexity**

This implementation of the Bloom filter completely follows the bit-wise design and therefore has **linear time (*O(n)*) and space (*O(m)*) complexity**.

- Insertion and search methods do *k* iterations through each hash function (where *k* is the number of hash functions) and inside each hash function the time complexity is *O(1)*, therefore their time complexity overall is *O(k)*.
- The bit array size is *m* and therefore the space complexity for the bit array is *O(m)*.
- We also have a *k* number of hash functions stored inside the bloom filter so complexity for that context is *O(k)*.
