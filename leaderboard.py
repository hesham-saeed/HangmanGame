import os
import sqlite3
import player
conn = None
if os.path.isfile("leaderboard.db"):
    conn = sqlite3.connect('leaderboard.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE if not exists players (
    name text,
    score integer
    )""")

def add_player(player):
    with conn:
        cursor.execute("INSERT INTO players VALUES (:name, :score)",
                   {'name': player.name, 'score':player.score})

def get_players():
    cursor.execute("SELECT * FROM players ORDER BY score DESC")
    return cursor.fetchall()

def reset_leaderboard():
    with conn:
        cursor.execute("DELETE FROM players")

def close_connection():
    conn.close()
