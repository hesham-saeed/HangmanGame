import os.path
import random as rand

def preprocess_words(filename):
    return read_words_from_file(filename)
    #print(words_list[0])
    #print(words_list[-1])
    #return words_list
    #apply]ifficulty
    # with open(filename,"r") as file:
    #     words_list =file.read().splitlines()
    #     print(f"list size = {len(words_list)}")
    #     print(words_list[0])
    #     print(words_list[-1])

def read_words_from_file(filename):
    if os.path.isfile(filename):
        with open(filename,"r") as file:
            words = file.read().splitlines()
            filtered_words = [x for x in words if len(x) > 6]
            return filtered_words

def prepare_list(filename):
    return preprocess_words(filename)

def get_candidate_word():
    words = prepare_list("words.txt")
    rand_indx = rand.randint(0,len(words)-1)
    return words[rand_indx]
