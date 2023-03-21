import random
import player
import leaderboard
import words_easy_level_local
import words_hard_level_mysql

def get_candidate_word(words):
    rand_indx = random.randint(0,len(words)-1)
    return words[rand_indx]

def initialize_game(difficulty):
    candidateWord=""
    if difficulty == "h": #hard
        if words_hard_level_mysql.db_access:
            candidateWord=words_hard_level_mysql.get_candidate_word()
        else:
            candidateWord = words_easy_level_local.get_candidate_word()
    else:
        candidateWord = words_easy_level_local.get_candidate_word()
    word = print_word_as_puzzle(candidateWord)
    return word, candidateWord



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

def check_answer(question, solution, guessedLetter, lives):
    #print(f"checkanswer() {question} {solution}")
    q2 = ""
    for i in range(len(question)):
        if question[i] == '_' :
            if guessedLetter == solution[i]:
                #question[i] = guessedLetter
                q2 += guessedLetter
                q2 += question[i+1:]
                return q2, True, lives
            else:
                q2 += "_"
        else:
            q2 += question[i]

    lives -= 1
    return q2, False, lives

def main_game_loop(word, candidateWord, playerName):
    lives = 6
    correctAnswersInARow = 0
    maxCorrectAnswer = 0
    while (True):
        print_game_state(word)
        guessedLetter = input("Enter your guessed letter: ")
        word, isCorrect, lives = check_answer(word, candidateWord, guessedLetter, lives)
        if isCorrect:
                correctAnswersInARow += 1
                maxCorrectAnswer = max(maxCorrectAnswer, correctAnswersInARow)
        else:
            correctAnswersInARow = 0
        if isCorrect:
            print("you guessed that right!")
            print(print_hangman_stages(lives))
        else:
            print(f"wrong guess! lives remaining: {lives}")
            print(print_hangman_stages(lives))
        if word.find("_") == -1:
            print("Well done, you saved the man!")
            break
        elif lives <= 0:
            print("Too bad, you couldn't save him!")
            break
    p = player.Player(playerName, maxCorrectAnswer)
    leaderboard.add_player(p)
    return maxCorrectAnswer

def check_for_new_game():
    while (True):
        playAgain = input("Would you like to play again?\n New game:N\t\t Leaderboard:L\t\t Exit:E ")
        playAgain.lower()
        if playAgain == 'yes' or playAgain == 'y' or playAgain == 'n':
            return True
        elif playAgain.lower() == "l" or playAgain == "leaderboard":
            scores = leaderboard.get_players()
            printLeaderboard(scores)
        else:
            leaderboard.close_connection()
            if words_hard_level_mysql.db_access:
                words_hard_level_mysql.close_connection()
            return False

def print_hangman_stages(lives):
    stages = [ """
                    ---------
                    |       |
                    |       o
                    |      \\|/
                    |       |
                    |      / \\
                    -
                ""","""
                    ---------
                    |       |
                    |       o
                    |      \\|/
                    |       |
                    |      / 
                    -
                ""","""
                    ---------
                    |       |
                    |       o
                    |      \\|/
                    |       |
                    |      
                    -
                ""","""
                    ---------
                    |       |
                    |       o
                    |      \\|
                    |       |  
                    |      
                    -
                ""","""
                    ---------
                    |       |
                    |       o
                    |       |
                    |       |
                    |      
                    -
                ""","""
                    ---------
                    |       |
                    |       o
                    |       
                    |       
                    |      
                    -
                ""","""
                    ---------
                    |       |
                    |       
                    |      
                    |       
                    |      
                    -
                """
    ]
    return stages[lives]

def printLeaderboard(scores):
    print("************************")
    print("LEADERBOARD SCORES")
    print("************************")
    for score in scores:
        print(score[0] + "\t", score[1])

def start_game():
    playername = input("Enter your name: ")
    difficulty = input("Difficulty\t\t Easy:E\t\t Hard:H\t").lower()
    question, solution = initialize_game(difficulty)
    main_game_loop(question, solution, playername)
    if check_for_new_game():
        start_game()

if __name__ == '__main__':
    start_game()