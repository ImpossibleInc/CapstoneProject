import sqlite3
import pandas as pd

conn = sqlite3.connect('playerDatabase.sqlite')
c = conn.cursor()
df = pd.DataFrame()
conn.set_trace_callback(print)

clear_sql = "DROP TABLE IF EXISTS completeStats"
create_sql = """
CREATE TABLE completeStats (id INTEGER PRIMARY KEY, player_id INTEGER, name TEXT, position TEXT, year INTEGER, \
              age INTEGER, games_played INTEGER, games_started INTEGER, passing_completions INTEGER, passing_attempts INTEGER, \
              passing_yards INTEGER, passing_TDs INTEGER, interceptions INTEGER, rushing_attempts INTEGER, rushing_yards INTEGER, \
              yards_per_attempt REAL, rushing_TDs INTEGER, targets INTEGER, receptions INTEGER, receiving_yards INTEGER, \
              yards_per_reception REAL, receiving_TDs INTEGER, fumbles INTEGER, fumbles_lost INTEGER, two_point_conversions INTEGER, \
              two_point_passes INTEGER, fantasy_points REAL, prev_games_played INTEGER, prev_games_started INTEGER, prev_passing_completions INTEGER, prev_passing_attempts INTEGER, \
              prev_passing_yards INTEGER, prev_passing_TDs INTEGER, prev_interceptions INTEGER, prev_rushing_attempts INTEGER, prev_rushing_yards INTEGER, \
              prev_yards_per_attempt REAL, prev_rushing_TDs INTEGER, prev_targets INTEGER, prev_receptions INTEGER, prev_receiving_yards INTEGER, \
              prev_yards_per_reception REAL, prev_receiving_TDs INTEGER, prev_fumbles INTEGER, prev_fumbles_lost INTEGER, prev_two_point_conversions INTEGER, \
              prev_two_point_passes INTEGER, prev_fantasy_points REAL);
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
add_id_main = """
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
make_previous_year = """
CREATE TABLE previous_year (player_id INTEGER, prev_year INTEGER, prev_games_played INTEGER, prev_games_started INTEGER, prev_passing_completions INTEGER, prev_passing_attempts INTEGER, \
              prev_passing_yards INTEGER, prev_passing_TDs INTEGER, prev_interceptions INTEGER, prev_rushing_attempts INTEGER, prev_rushing_yards INTEGER, \
              prev_yards_per_attempt REAL, prev_rushing_TDs INTEGER, prev_targets INTEGER, prev_receptions INTEGER, prev_receiving_yards INTEGER, \
              prev_yards_per_reception REAL, prev_receiving_TDs INTEGER, prev_fumbles INTEGER, prev_fumbles_lost INTEGER, prev_two_point_conversions INTEGER, \
              prev_two_point_passes INTEGER, prev_fantasy_points REAL);
"""
populate_previous_year = """
INSERT INTO previous_year
SELECT player_id, year, games_played, games_started, passing_completions,
       passing_attempts, passing_yards, passing_TDs, interceptions, 
       rushing_attempts, rushing_yards, yards_per_attempt, rushing_TDs,
       targets, receptions, receiving_yards, yards_per_reception,
       receiving_TDs, fumbles, fumbles_lost, two_point_conversions,
       two_point_passes, fantasy_points
FROM completeStats;
"""
add_prev_main ="""
UPDATE completeStats
SET (prev_games_played, prev_games_started, prev_passing_completions, prev_passing_attempts,
    prev_passing_yards, prev_passing_TDs, prev_interceptions, prev_rushing_attempts, prev_rushing_yards,
    prev_yards_per_attempt, prev_rushing_TDs, prev_targets, prev_receptions, prev_receiving_yards,
    prev_yards_per_reception, prev_receiving_TDs, prev_fumbles, prev_fumbles_lost, prev_two_point_conversions,
    prev_two_point_passes, prev_fantasy_points) = (
    SELECT prev_games_played, prev_games_started, prev_passing_completions, prev_passing_attempts,
    prev_passing_yards, prev_passing_TDs, prev_interceptions, prev_rushing_attempts, prev_rushing_yards,
    prev_yards_per_attempt, prev_rushing_TDs, prev_targets, prev_receptions, prev_receiving_yards,
    prev_yards_per_reception, prev_receiving_TDs, prev_fumbles, prev_fumbles_lost, prev_two_point_conversions,
    prev_two_point_passes, prev_fantasy_points
    FROM previous_year
    WHERE previous_year.player_id = completeStats.player_id
      AND previous_year.prev_year = (completeStats.year - 1)
    )
WHERE EXISTS (
    SELECT 1
    FROM previous_year
    WHERE previous_year.player_id = completeStats.player_id
      AND previous_year.prev_year = (completeStats.year - 1)
);
"""
drop_prev = "DROP TABLE IF EXISTS previous_year"

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

def create_prev():
    c.execute(make_previous_year)

def populate_prev():
    c.execute(populate_previous_year)
    conn.commit()

def fill_prev():
    print("Running add_prev_main...")
    print(add_prev_main)  # Log the query being executed
    c.execute(add_prev_main)
    conn.commit()
    print("Finished running add_prev_main.")

def unique_players():
    c.execute(populate_player_id)

def drop_temp():
    c.execute(drop_extra)
    c.execute(drop_prev)

def clear_dupes():
    c.execute(delete_dupes)

def fill_id():
    c.execute(add_id_main)

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
    conn.commit()
    create_prev()
    populate_prev()
    conn.commit()
    fill_prev()
    conn.commit()
    drop_temp()
    conn.commit()