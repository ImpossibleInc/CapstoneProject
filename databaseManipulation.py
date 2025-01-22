import sqlite3
import pandas as pd

conn = sqlite3.connect('playerDatabase.sqlite')
c = conn.cursor()
df = pd.DataFrame()

clear_sql = "DROP TABLE IF EXISTS completeStats"
create_sql = """
CREATE TABLE completeStats (id INTEGER PRIMARY KEY, player_id INTEGER, name TEXT, position TEXT, year INTEGER, \
              age INTEGER, games_played INTEGER, games_started INTEGER, passing_completions INTEGER, passing_attempts INTEGER, \
              passing_yards INTEGER, passing_TDs INTEGER, interceptions INTEGER, rushing_attempts INTEGER, rushing_yards INTEGER, \
              yards_per_attempt REAL, rushing_TDs INTEGER, targets INTEGER, receptions INTEGER, receiving_yards INTEGER, \
              yards_per_reception REAL, receiving_TDs INTEGER, fumbles INTEGER, fumbles_lost INTEGER, two_point_conversions INTEGER, \
              two_point_passes INTEGER, fantasy_points REAL);
              """

create_player_id = """
CREATE TABLE player_id_made (player_id INTEGER PRIMARY KEY, name TEXT, birth_year INTEGER);
"""
populate_player_id = """
INSERT INTO player_id_made 
SELECT player_id, name, (year - age) AS 'birth_year' 
FROM completeStats 
GROUP BY name, birth_year;
"""
delete_dupes = """
DELETE FROM completeStats WHERE id NOT IN (SELECT MIN(id) FROM completeStats GROUP BY name, year, position, age);
"""
update_main = """
UPDATE completeStats
SET player_id = (
    SELECT player_id
    FROM player_id_made
    WHERE player_id_made.name = completeStats.name
      AND player_id_made.birth_year = (completeStats.year - completeStats.age)
)
WHERE EXISTS (
    SELECT 1
    FROM player_id_made
    WHERE player_id_made.name = completeStats.name
      AND player_id_made.birth_year = (completeStats.year - completeStats.age)
);
"""
drop_extra = "DROP TABLE IF EXISTS player_id_made"

def clear_main():
    c.execute(clear_sql)

def create_main():
    c.execute(create_sql)

def fill_main(df):
    for row in df.itertuples():
        insert_sql = f"INSERT INTO completeStats (name, position, year, age, games_played, games_started, passing_completions, passing_attempts, \
        passing_yards, passing_TDs, interceptions, rushing_attempts, rushing_yards, yards_per_attempt, rushing_TDs, targets, receptions, receiving_yards, \
        yards_per_reception, receiving_TDs, fumbles, fumbles_lost, two_point_conversions, two_point_passes, fantasy_points) VALUES ('{row[3]}', '{row[5]}', {row[1]}, \
        {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}, {row[13]}, {row[14]}, {row[15]}, {row[16]}, {row[17]}, {row[18]}, {row[19]}, {row[20]}, \
        {row[21]}, {row[22]}, {row[23]}, {row[24]}, {row[25]}, {row[26]}, {row[29]})"
        c.execute(insert_sql)

def create_id():
    c.execute(create_player_id)

def unique_players():
    c.execute(populate_player_id)

def drop_temp():
    c.execute(drop_extra)

def clear_dupes():
    c.execute(delete_dupes)

def fill_id():
    c.execute(update_main)

def full_build (df):
    clear_main()
    drop_temp()
    conn.commit()
    create_main()
    fill_main(df)
    clear_dupes()
    conn.commit()
    create_id()
    unique_players()
    conn.commit()
    fill_id()
    drop_temp()
    conn.commit()