'''
    Check whether the given word is in the know words dictionary or not
    this runs sequentially
'''
from hashlib import sha512
import os
import time

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
    known_words = {hash_word(word) for word in words}
    print(f'Done with {len(known_words)} hashes')
    
    


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Overall time taken to run the main method : {round(finish-start, 2)} second(s)')
