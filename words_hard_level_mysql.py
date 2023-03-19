import os
import random

import mysql.connector

if os.path.isfile("credentials.txt"):
    with open("credentials.txt", "r") as file:
        lines = file.readlines()

configs = {}
if os.path.isfile("credentials.txt"):
    with open("credentials.txt") as myfile:
        for line in myfile:
            name, val = line.partition("=")[::2]
            configs[name.strip()] = val.strip()

db = mysql.connector.connect(
    host=configs["host"],
    user=configs["user"],
    passwd=configs["passwd"],
    database=configs["database"]
)
cursor = db.cursor()
cursor.execute("""DROP TABLE words""")
cursor.execute("""CREATE TABLE if not exists words (
    word TEXT,
    length INT
    )""")
cursor.execute("SELECT COUNT(*) FROM words")
if cursor.fetchone()[0] == 0:
    query = 'INSERT INTO words VALUES(%s,%s)'
    filename = "10kwords.txt"
    listOfWords = []
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                word = line.strip()
                length = len(word)
                listOfWords.append(tuple([word,length]))
    cursor.executemany(query, listOfWords)
    db.commit()

def get_candidate_word():
    cursor.execute("SELECT * FROM words order by length DESC LIMIT 200")
    words = cursor.fetchall()
    rand_indx = random.randint(0,200)
    return words[rand_indx][0]
def close_connection():
    db.close()