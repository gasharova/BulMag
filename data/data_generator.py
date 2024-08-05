import random
import string

# Methods acting as a provider/loader for each data type

def get_natural_language_words(n):
    filepath = './data/words_alpha.txt' 
    words = []
    with open(filepath, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            word = line.strip()

            # Add lines from the dataset until n
            if line_number <= n:
                words.append(word)

            # If the dataset still contains unadded elements:
            else:
                # Replace current elements in the pool randomly to randomize the result
                r = random.randint(0, line_number - 1)
                if r < n:
                    words[r] = word

        dataset_size = len(words)
        # If the requested n is larger than the dataset size, duplicate words
        # This is ok as it reflects real scenario (duplicates are normal for real data)
        if n > len(words):
            number_of_extra_words_needed = n-dataset_size
            extra_words = random.choices(words, k=number_of_extra_words_needed)
            words.extend(extra_words)
    return words

def get_random_strings(n, max_length=100):
    random_strings = []
    for _ in range(n):
        # Randomize length of each random string
        string_length = random.randint(1, max_length)
        # Get the random string with the randomized current length
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=string_length))
        # Append to the list of random strings
        random_strings.append(random_string)
    return random_strings

def get_dna_sequences(n):
    filepath = './data/Coding_NonCoding_DNA_Sequences' 
    sequences = []
    with open(filepath, 'r') as file:
        next(file) # Skip header
        for line_number, line in enumerate(file, start=1):
            line_uncleaned = line.strip()
            parts = line_uncleaned.split(',')
            sequence = parts[2]

            # Add lines from the dataset until n
            if line_number <= n:
                sequences.append(sequence)

            # If the dataset still contains unadded elements:
            else:
                # Replace current elements in the pool randomly to randomize the result
                r = random.randint(0, line_number - 1)
                if r < n:
                    sequences[r] = sequence

        dataset_size = len(sequences)
        # If the requested n is larger than the dataset size, duplicate sequences
        # This is ok as it reflects real scenario (duplicates are normal for real data)
        if n > len(sequences):
            number_of_extra_words_needed = n-dataset_size
            extra_words = random.choices(sequences, k=number_of_extra_words_needed)
            sequences.extend(extra_words)
    return sequences

def get_urls(n):
    url_list = []
    domains = [
        "https://www.example.net",
        "https://uhasselt.be",
        "https://9gag.com",
        "https://isitchristmas.com"
    ]

    # Structure will follow domain.name/pageX?articleid=Y
    # in order to simulate directories and queries for more realistic data
    for _ in range(n):
        domain = random.choice(domains)
        page_number = random.randint(1, 100)
        article_number = random.randint(1, 10000)
        url = f"{domain}/page{page_number}?article_id={article_number}"
        url_list.append(url)

    # Mix the results
    random.shuffle(url_list)
    return url_list
