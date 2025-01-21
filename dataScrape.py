import sqlite3
from logging import fatal

import pandas as pd
import numpy as np
import random
import time

seasons = [str(season) for season in range(2005,2024)]

fantasy_scores = pd.DataFrame()

for season in seasons:
    url = 'https://www.pro-football-reference.com/years/' + season + '/fantasy.htm#fantasy'
    print(url)
    fantasy_season = pd.read_html(url, header = 1, attrs={'id': 'fantasy' })[0]
    columns = ['Player','Tm','FantPos','Age','Games Played','Games Started','Passes Completed','Pass Attempts','Passing Yds','Passing TD','Passes Intercepted','Rushing Att','Rushing Yds','Yds/Rushing Att','Rushing TD','Targets','Receptions','Receiving Yds','Yds/Reception','Receiving TD','Fumbles','Fumbles Lost','2-pt. Conv. Made','Fantasy Point (PPR)']
    fantasy_season = fantasy_season.loc[:,columns].iloc[:, :2]
    fantasy_season.insert(0, 'Season', season)
    print(fantasy_season)
    fantasy_scores = pd.concat([fantasy_scores, fantasy_season], ignore_index=True)
    time.sleep(random.randint(5,7))

print(fantasy_scores)
'''
conn = sqlite3.connect('playerDatabase.sqlite')
c = conn.cursor()


id = 0
def getStats(url):

id = id + 1
name = ''
position = ''
year =
age =
games_played =
games_started =
passing_completions =
passing_attempts =
passing_yards =
passing_TDs =
interceptions =
rushing_attempts =
rushing_yards =
yards_per_attempt =
rushing_TDs =
targets =
receptions =
receiving_yards =
yards_per_reception =
receiving_TDs =
fumbles =
fumbles_lost =
two_point_conversions =
fantasy_points =
'''

