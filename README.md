# BulMag
Bloom filter implementation and analysis

Members:
@gasharova @Istvan1996


# Usage

Please clone the repository locally in order to use the files as official package uploading is not planned in the near future.
The Bloom filter can be imported as in the following example:

```
from bloom_filter.bloom_filter import BloomFilter
```

## Dependencies

bitarray        2.9.2
cityhash        0.4.7
contourpy       1.2.1
cycler          0.12.1
fonttools       4.53.1
kiwisolver      1.4.5
matplotlib      3.9.0
mmh3            4.1.0
numpy           2.0.1
packaging       24.1
pillow          10.4.0
pip             22.3.1
pyparsing       3.1.2
python-dateutil 2.9.0.post0
setuptools      65.5.0
six             1.16.0


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

**6. Benchmarking time for Bloom filter and other relevant data structures**

HPC was extensively used to satisfy benchmarking requirements. Along with the Bloom filter, Hash table and Python's built-in dynamic list[] structures were also benchmarked for comparison. Benchmarking was first executed with a smaller sample locally, after which HPC's architecture was used with a larger data sample. Local virtual environment was set up on the remote machine to achieve better modularization during project execution. The resulting JSON file was downloaded from the server and visualised. All 4 data categories were used for the experiment. The total result are 2 sets of 8 graphs (add and search for each of the 4 data types) which allow for further elaboration on each data structure's benefits and behavior. 

**7. Exploring FP rate as a function of words inserted**

For this question, all 4 data providers were used in order to plot 4 plots. Data was visualised with focus on FP rate up to the number of inserted elements for which the filter is designed, versus FP rate when more elements are incrementally inserted. All scripts and graphs are available in the Jupyter notebook.

**8. Exploring the compression rate of a Bloom filter**

For this question, the compression rate of the filter was analyzed as a function of the theoretical FP rate and the expected number of elements.
Possible room for improvement could be adding analysis as a function of the observed FP rate (via simulation as in question 7 above).
Calculations for m were performed in order to build Bloom filters and simulate all variables.
3D plots were created in order to be able to map all 3 variables. Since the compression rate is of interest, it has been assigned the Y axis for those plots.
Extra details can be seen with multiple points of view in the graphs.
Again we are using here 4 types of data and all scripts and graphs are available in the Jupyter notebook.

# Summary of conclusions

The theoretical and observed error rate of the Bloom filter, when decreasing leads to a more dense Bloom filter, and vice versa. Increasing the number of bits in the internal implementation array can help relieve this effect, but on the other hand, it requires more space. The Bloom Filter performed the best at searching speed and relatively well for adding speed when benchmarked against hash maps and dynamic python lists.