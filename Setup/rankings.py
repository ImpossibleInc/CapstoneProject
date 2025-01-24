from Setup.databaseManipulation import create_rankings
import pandas as pd
import sqlite3

def make_rankings(num):
    conn = sqlite3.connect('playerDatabase.sqlite')

    create_rankings(num)
    conn.commit()

    rankings = pd.read_sql_query("SELECT * FROM currentPlayers", conn)
    print(rankings)

def print_rankings():
    conn = sqlite3.connect('playerDatabase.sqlite')
    rankings = pd.read_sql_query("SELECT * FROM currentPlayers", conn)
    print(rankings.to_string())
