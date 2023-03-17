import random
from words import preprocess_words

lives = 25
answerWord = ""

def get_candidate_word(words):
    rand_indx = random.randint(0,len(words)-1)
    return words[rand_indx]

def initialize_game():
    print("calling prepareList()")
    words = prepare_list("words.txt")
    candidateWord = get_candidate_word(words)
    word = print_word_as_puzzle(candidateWord)
    return word, candidateWord

def prepare_list(filename):
    return preprocess_words(filename)

def print_word_as_puzzle(word):
    revealedCharPos = random.randint(0,len(word)-1)
    answerWord =""
    for i in range(len(word)):
        if i == revealedCharPos:
            #print(word[i], end='', flush=True)
            answerWord += word[i]
        else:
            answerWord += "_"
            #print('_', end='', flush=True)
    return answerWord

def print_game_state(word):
    for i in range(len(word)):
        print(word[i], end='', flush=True)
    print()

# Press the green button in the gutter to run the script.
def check_answer(question, solution, guessedLetter):
    #print(f"checkanswer() {question} {solution}")
    global lives
    q2 = ""
    for i in range(len(question)):
        if question[i] == '_' :
            if guessedLetter == solution[i]:
                #question[i] = guessedLetter
                q2 += guessedLetter
                q2 += question[i+1:]
                return q2, True
            else:
                q2 += "_"
        else:
            q2 += question[i]

    lives -= 1
    return q2, False

def main_game_loop(word, candidateWord):
    while (True):
        print_game_state(word)
        guessedLetter = input("Enter your guessed letter: ")
        word, isCorrect = check_answer(word, candidateWord, guessedLetter)
        if isCorrect:
            print("you guessed that right!")
        else:
            print("wrong guess!")
        if word.find("_") == -1:
            print("Well done, you saved the man!")
            break
        elif lives <= 0:
            print("Too bad, you couldn't save him!")
            break

def start_game():
    question, solution = initialize_game()
    main_game_loop(question, solution)

if __name__ == '__main__':
    start_game()