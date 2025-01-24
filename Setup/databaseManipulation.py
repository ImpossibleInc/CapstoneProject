import sqlite3

conn = sqlite3.connect('playerDatabase.sqlite')
c = conn.cursor()

#completeStats
def clear_main():
    c.execute("DROP TABLE IF EXISTS completeStats")

def create_main():
    c.execute(f"CREATE TABLE completeStats (id INTEGER PRIMARY KEY, player_id INTEGER, name TEXT, position TEXT, year INTEGER, \
              age INTEGER, games_played INTEGER, games_started INTEGER, passing_completions INTEGER, passing_attempts INTEGER, \
              passing_yards INTEGER, passing_TDs INTEGER, interceptions INTEGER, rushing_attempts INTEGER, rushing_yards INTEGER, \
              yards_per_attempt REAL, rushing_TDs INTEGER, targets INTEGER, receptions INTEGER, receiving_yards INTEGER, \
              yards_per_reception REAL, receiving_TDs INTEGER, fumbles INTEGER, fumbles_lost INTEGER, two_point_conversions INTEGER, \
              two_point_passes INTEGER, fantasy_points REAL, prev_games_played INTEGER, prev_games_started INTEGER, prev_passing_completions INTEGER, \
              prev_passing_attempts INTEGER, prev_passing_yards INTEGER, prev_passing_TDs INTEGER, prev_interceptions INTEGER, prev_rushing_attempts INTEGER, \
              prev_rushing_yards INTEGER, prev_yards_per_attempt REAL, prev_rushing_TDs INTEGER, prev_targets INTEGER, prev_receptions INTEGER, \
              prev_receiving_yards INTEGER, prev_yards_per_reception REAL, prev_receiving_TDs INTEGER, prev_fumbles INTEGER, prev_fumbles_lost INTEGER, \
              prev_two_point_conversions INTEGER, prev_two_point_passes INTEGER, prev_fantasy_points REAL);")

def fill_main(df):
    for row in df.itertuples():
        c.execute(f"INSERT INTO completeStats (name, position, year, age, games_played, games_started, passing_completions, passing_attempts, \
        passing_yards, passing_TDs, interceptions, rushing_attempts, rushing_yards, yards_per_attempt, rushing_TDs, targets, receptions, receiving_yards, \
        yards_per_reception, receiving_TDs, fumbles, fumbles_lost, two_point_conversions, two_point_passes, fantasy_points) VALUES ('{row[3]}', '{row[5]}', {row[1]}, \
        {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}, {row[13]}, {row[14]}, {row[15]}, {row[16]}, {row[17]}, {row[18]}, {row[19]}, {row[20]}, \
        {row[21]}, {row[22]}, {row[23]}, {row[24]}, {row[25]}, {row[26]}, {row[29]})")

def fill_prev():
    c.execute("""
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
""")
    conn.commit()

def clear_dupes():
    c.execute("DELETE FROM completeStats WHERE id NOT IN (SELECT MIN(id) FROM completeStats GROUP BY name, year, position, age);")

def zero_out():
    c.execute("""
UPDATE completeStats
SET
    prev_games_played = COALESCE(prev_games_played, 0),
    prev_games_started = COALESCE(prev_games_started, 0),
    prev_passing_completions = COALESCE(prev_passing_completions, 0),
    prev_passing_attempts = COALESCE(prev_passing_attempts, 0),
    prev_passing_yards = COALESCE(prev_passing_yards, 0),
    prev_passing_TDs = COALESCE(prev_passing_TDs, 0),
    prev_interceptions = COALESCE(prev_interceptions, 0),
    prev_rushing_attempts = COALESCE(prev_rushing_attempts, 0),
    prev_rushing_yards = COALESCE(prev_rushing_yards, 0),
    prev_yards_per_attempt = COALESCE(prev_yards_per_attempt, 0),
    prev_rushing_TDs = COALESCE(prev_rushing_TDs, 0),
    prev_targets = COALESCE(prev_targets, 0),
    prev_receptions = COALESCE(prev_receptions, 0),
    prev_receiving_yards = COALESCE(prev_receiving_yards, 0),
    prev_yards_per_reception = COALESCE(prev_yards_per_reception, 0),
    prev_receiving_TDs = COALESCE(prev_receiving_TDs, 0),
    prev_fumbles = COALESCE(prev_fumbles, 0),
    prev_fumbles_lost = COALESCE(prev_fumbles_lost, 0),
    prev_two_point_conversions = COALESCE(prev_two_point_conversions, 0),
    prev_two_point_passes = COALESCE(prev_two_point_passes, 0),
    prev_fantasy_points = COALESCE(prev_fantasy_points, 0)
WHERE
    prev_games_played IS NULL OR
    prev_games_started IS NULL OR
    prev_passing_completions IS NULL OR
    prev_passing_attempts IS NULL OR
    prev_passing_yards IS NULL OR
    prev_passing_TDs IS NULL OR
    prev_interceptions IS NULL OR
    prev_rushing_attempts IS NULL OR
    prev_rushing_yards IS NULL OR
    prev_yards_per_attempt IS NULL OR
    prev_rushing_TDs IS NULL OR
    prev_targets IS NULL OR
    prev_receptions IS NULL OR
    prev_receiving_yards IS NULL OR
    prev_yards_per_reception IS NULL OR
    prev_receiving_TDs IS NULL OR
    prev_fumbles IS NULL OR
    prev_fumbles_lost IS NULL OR
    prev_two_point_conversions IS NULL OR
    prev_two_point_passes IS NULL OR
    prev_fantasy_points IS NULL;
    """)

def fill_id():
    c.execute("""
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
    );"""
)

#player_id
def create_id():
    c.execute("CREATE TABLE player_id_made (player_id INTEGER PRIMARY KEY, name TEXT, birth_year INTEGER);")

def unique_players():
    c.execute("""INSERT INTO player_id_made 
                 SELECT player_id, name, (year - age) AS 'birth_year' 
                 FROM completeStats 
                 GROUP BY name, birth_year;""")

#previous_year
def create_prev():
    c.execute("""
CREATE TABLE previous_year (player_id INTEGER, prev_year INTEGER, prev_games_played INTEGER, prev_games_started INTEGER, prev_passing_completions INTEGER, prev_passing_attempts INTEGER, \
              prev_passing_yards INTEGER, prev_passing_TDs INTEGER, prev_interceptions INTEGER, prev_rushing_attempts INTEGER, prev_rushing_yards INTEGER, \
              prev_yards_per_attempt REAL, prev_rushing_TDs INTEGER, prev_targets INTEGER, prev_receptions INTEGER, prev_receiving_yards INTEGER, \
              prev_yards_per_reception REAL, prev_receiving_TDs INTEGER, prev_fumbles INTEGER, prev_fumbles_lost INTEGER, prev_two_point_conversions INTEGER, \
              prev_two_point_passes INTEGER, prev_fantasy_points REAL);
""")

def populate_prev():
    c.execute("""
INSERT INTO previous_year
SELECT player_id, year, games_played, games_started, passing_completions,
       passing_attempts, passing_yards, passing_TDs, interceptions, 
       rushing_attempts, rushing_yards, yards_per_attempt, rushing_TDs,
       targets, receptions, receiving_yards, yards_per_reception,
       receiving_TDs, fumbles, fumbles_lost, two_point_conversions,
       two_point_passes, fantasy_points
FROM completeStats;
""")
    conn.commit()

#drop previous year and player id
def drop_temp():
    c.execute("DROP TABLE IF EXISTS player_id_made")
    c.execute("DROP TABLE IF EXISTS previous_year")

#full build for dataScrape
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
    zero_out()
    conn.commit()


#linear model
def create_lms():
    c.execute(f"CREATE TABLE linear_model (position TEXT, age_coef REAL, games_played_coef REAL, games_started_coef REAL,\
                           pass_comp_coef REAL, pass_att_coef REAL, pass_yds_coef REAL, pass_TD_coef REAL,\
                           intercept_coef REAL, rush_att_coef REAL, rush_yds_coef REAL, y_per_a_coef REAL,\
                           rush_TD_coef REAL, tar_coef REAL, rec_coef REAL, rec_yds_coef REAL, y_per_rec_coef REAL,\
                           rec_TD_coef REAL, fmbl_coef REAL, fmbl_l_coef REAL, two_pt_conv_coef REAL,\
                           two_pt_pass_coef, fantasy_coef REAL, intercept);")

def fill_lms(string, array, double):
    c.execute(f"INSERT INTO linear_model (position, age_coef, games_played_coef, games_started_coef, \
                          pass_comp_coef, pass_att_coef, pass_yds_coef, pass_TD_coef, \
                          intercept_coef, rush_att_coef, rush_yds_coef, y_per_a_coef, \
                          rush_TD_coef, tar_coef, rec_coef, rec_yds_coef, y_per_rec_coef, \
                          rec_TD_coef, fmbl_coef, fmbl_l_coef, two_pt_conv_coef, \
                          two_pt_pass_coef, fantasy_coef, intercept) VALUES ('{string}', {array[0]}, {array[1]}, {array[2]}, {array[3]},\
                          {array[4]}, {array[5]}, {array[6]}, {array[7]}, {array[8]}, {array[9]}, {array[10]},\
                          {array[11]}, {array[12]}, {array[13]}, {array[14]}, {array[15]}, {array[16]}, {array[17]},\
                          {array[18]}, {array[19]}, {array[20]}, {array[21]}, {double})")
    conn.commit()

def drop_lms():
    c.execute(f"DROP TABLE IF EXISTS linear_model;")
    conn.commit()

#current players
def create_current_player():
    c.execute("""
    CREATE TABLE currentPlayers (player_id INTEGER, name TEXT, position TEXT,
                             projected_rank INTEGER, actual_rank INTEGER, projected_fantasy_score_by_position REAL,
                             projected_fantasy_score_by_full REAL, actual_fantasy_score REAL, difference REAL, age INTEGER, prev_games_played INTEGER, prev_games_started INTEGER, prev_passing_completions INTEGER, prev_passing_attempts INTEGER,
                             prev_passing_yards INTEGER, prev_passing_TDs INTEGER, prev_interceptions INTEGER, prev_rushing_attempts INTEGER, prev_rushing_yards INTEGER,
                             prev_yards_per_attempt REAL, prev_rushing_TDs INTEGER, prev_targets INTEGER, prev_receptions INTEGER, prev_receiving_yards INTEGER,
                             prev_yards_per_reception REAL, prev_receiving_TDs INTEGER, prev_fumbles INTEGER, prev_fumbles_lost INTEGER, prev_two_point_conversions INTEGER,
                             prev_two_point_passes INTEGER, prev_fantasy_points REAL);
    """)
    conn.commit()

def fill_current_player(num):
    c.execute(f"INSERT INTO currentPlayers\
    SELECT player_id, name, position, NULL AS projected_rank, NULL AS actual_rank, NULL AS projected_fantasy_score_by_position,\
      NULL AS projected_fantasy_score_by_full, fantasy_points AS actual_fantasy_score, NULL AS difference,\
      age, prev_games_played, prev_games_started, prev_passing_completions, prev_passing_attempts,\
      prev_passing_yards, prev_passing_TDs, prev_interceptions, prev_rushing_attempts,\
      prev_rushing_yards, prev_yards_per_attempt, prev_rushing_TDs, prev_targets, prev_receptions,\
      prev_receiving_yards, prev_yards_per_reception, prev_receiving_TDs, prev_fumbles,\
      prev_fumbles_lost, prev_two_point_conversions, prev_two_point_passes, prev_fantasy_points\
    FROM completeStats\
    WHERE year = {num};")
    conn.commit()

def actual_rank():
    c.execute("""
    UPDATE currentPlayers
    SET actual_rank = (
      SELECT COUNT(*)
      FROM currentPlayers AS sub
      WHERE sub.position = currentPlayers.position
        AND sub.actual_fantasy_score >= currentPlayers.actual_fantasy_score
    )
    WHERE position IN ('RB', 'WR', 'QB', 'TE', 'FB');
    """)

def projected_on_full():
    c.execute("""
    UPDATE currentPlayers
    SET projected_fantasy_score_by_full = (intercept + age_coef * age + games_played_coef * prev_games_played + games_started_coef * prev_games_started
      + pass_comp_coef * prev_passing_completions + pass_att_coef * prev_passing_attempts + pass_yds_coef * prev_passing_yards + pass_TD_coef *
      prev_passing_TDs + intercept_coef * prev_interceptions + rush_att_coef * prev_rushing_attempts + rush_yds_coef * prev_rushing_yards +
      y_per_a_coef * prev_yards_per_attempt + rush_TD_coef * prev_rushing_TDs + tar_coef * prev_targets + rec_coef * prev_receptions +
      rec_yds_coef * prev_receiving_yards + y_per_rec_coef * prev_yards_per_reception + rec_yds_coef * prev_receiving_TDs + fmbl_coef * prev_fumbles
      + fmbl_l_coef * prev_fumbles_lost + two_pt_conv_coef * prev_two_point_conversions + two_pt_pass_coef * prev_two_point_passes +
      fantasy_coef * prev_fantasy_points)
    FROM linear_model
    WHERE linear_model.position = 'Total Data';
    """)

def projected_on_pos():
    c.execute("""
    UPDATE currentPlayers
    SET projected_fantasy_score_by_position = (intercept + age_coef * age + games_played_coef * prev_games_played + games_started_coef * prev_games_started
      + pass_comp_coef * prev_passing_completions + pass_att_coef * prev_passing_attempts + pass_yds_coef * prev_passing_yards + pass_TD_coef *
      prev_passing_TDs + intercept_coef * prev_interceptions + rush_att_coef * prev_rushing_attempts + rush_yds_coef * prev_rushing_yards +
      y_per_a_coef * prev_yards_per_attempt + rush_TD_coef * prev_rushing_TDs + tar_coef * prev_targets + rec_coef * prev_receptions +
      rec_yds_coef * prev_receiving_yards + y_per_rec_coef * prev_yards_per_reception + rec_yds_coef * prev_receiving_TDs + fmbl_coef * prev_fumbles
      + fmbl_l_coef * prev_fumbles_lost + two_pt_conv_coef * prev_two_point_conversions + two_pt_pass_coef * prev_two_point_passes +
      fantasy_coef * prev_fantasy_points)
    FROM linear_model
    WHERE linear_model.position = currentPlayers.position;
    """)

def set_difference():
    c.execute("""
    UPDATE currentPlayers
    SET difference = (actual_fantasy_score - projected_fantasy_score_by_position)
    WHERE difference IS NULL;
    """)

def projected_rank():
    c.execute("""
    UPDATE currentPlayers
    SET projected_rank = (
      SELECT COUNT(*)
      FROM currentPlayers AS sub
      WHERE sub.position = currentPlayers.position
        AND sub.projected_fantasy_score_by_position >= currentPlayers.projected_fantasy_score_by_position
    )
    WHERE position IN ('RB', 'WR', 'QB', 'TE', 'FB');
    """)

def clean_current():
    c.execute("""
    CREATE TABLE new_currentPlayers AS
    SELECT
    player_id, name, position,
    projected_rank, actual_rank, projected_fantasy_score_by_position,
    projected_fantasy_score_by_full, actual_fantasy_score, difference
    FROM currentPlayers;
    """)
    c.execute("DROP TABLE currentPlayers;")
    c.execute("ALTER TABLE new_currentPlayers RENAME TO currentPlayers;")

def drop_current():
    c.execute(f"DROP TABLE IF EXISTS currentPlayers;")
    conn.commit()

def create_rankings(num):
    drop_current()
    create_current_player()
    fill_current_player(num)
    actual_rank()
    projected_on_full()
    projected_on_pos()
    set_difference()
    projected_rank()
    conn.commit()
    clean_current()
    conn.commit()

#shutdown
def db_close():
    conn.close()