'''
    Check whether the given word is in the know words dictionary or not
    this runs sequentially
'''
from hashlib import sha512
import os
import time
from math import ceil
import concurrent.futures

def hash_word(word:str) -> str:
    '''
        Calculate and retiurn the hash of the word
    '''
    hash_object = sha512()
    byte_data = word.encode('utf-8')
    hash_object.update(byte_data)
    return hash_object.hexdigest()

def load_words(path:str) -> list[str]:
    '''
        Loads words from the text file inta list
    '''
    with open(path, encoding='utf-8') as file:
        return file.readlines()

def test_chunksize(words : list[str], size:int, number_of_processes : int) -> None:
    '''
        Test multiple chunk sizes to find out the optimal chunk size
    '''
    time1 = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(number_of_processes) as executor:
        _ = set(executor.map(hash_word, words, chunksize=size))
    time2 = time.perf_counter()
    total = time2 - time1
    print(f'Chunk Size : {size} Time Taken : {total:.3f} seconds')

def main()->None:
    '''
        Main method to execute
    '''
    # load the file of words into a python list
    relative_path: str = r'\src\data\1m_words.txt'
    full_path:  str = os.getcwd() + relative_path

    words = load_words(full_path)
    print(f'Loaded {len(words)} words from {full_path}')

    # Hash all known words
    number_of_processes : int = 4 # matches with the physical CPUs in the system
    base = ceil(len(words)/number_of_processes)
    sizes = [base, 100000, 50000, 10000, 5000, 1000, 100]
    for size in sizes:
        test_chunksize(words, size, number_of_processes)
    
        
    # print(f'Done with {len(known_words)} hashes')

if __name__ == '__main__':
    main()
    
