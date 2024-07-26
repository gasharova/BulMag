# BulMag
Bloom filter implementation and analysis

Members:
@gasharova @Istvan1996

# Summary per requirement point

**1. Version control and contributions tracking**

The code collaboration was done on GitHub. Commit messages followed structural and semantic guidelines for good practices. This READme file was created for more details on directories, setup, and way of working.

**2. Implementation approach**

This Bloom filter was implemented using an _object-oriented_ _(OO)_ approach. This was decided since we were looking at multiple different OO principles: encapsulation (since we don't want to mess with filter internals regarding bit_array, and each filter will have immutable attributes i.e. size due to design), polymorphism/inheritance (for each hash function, we have a common _hash()_ method inherited from the base, so we can hash a key without caring what's the algorithm behind it), abstraction (only functions for adding and checking are public).

Comments are present in the code files for further elaboration.

__ __init__ __.py files were created in the directories to ensure the parser treats them like modules.

Seeding (defaulted to 0) was added to each hash function for reproducibility and extra experimenting. A list of hash functions is passed to the filter class at function definition, allowing for modularity and flexibility by switching between functions we like without changing the internal implementation. Not all functions may be used, but the parameter _k_ is calculated for our filter design, and the _k_ functions are extracted and used.

Since different hash functions of different bit sizes are used, hash length is normalized inside the Bloom Filter.

**3. Testing**

Implementation is tested using basic unit tests.
For the hash functions, all of them use external libraries with many contributors and downloads and are maintained and tested by the Python community.
For the filter itself, tests were added for the addition and lookup procedures. 

