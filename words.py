import os.path
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
            return file.read().splitlines()

