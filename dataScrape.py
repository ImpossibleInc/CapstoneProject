import pandas as pd
import numpy as np
import random
import time

from databaseManipulation import full_build

seasons = [str(season) for season in range(2005,2025)]

fantasy_scores = pd.DataFrame()

for season in seasons:
    url = 'https://www.pro-football-reference.com/years/' + season + '/fantasy.htm#fantasy'
    print(url)
    fantasy_season = pd.read_html(url, header = 1, attrs={'id': 'fantasy' })[0]
    fantasy_season.insert(0, 'Season', season)
    fantasy_season = fantasy_season.fillna(0)
    fantasy_season = fantasy_season[fantasy_season['2PM'] != '2PM']
    fantasy_season['Player'] = fantasy_season['Player'].str.replace("'", "''")
    fantasy_season['Player'] = fantasy_season['Player'].str.replace("*", "")
    fantasy_season['Player'] = fantasy_season['Player'].str.replace("+", "")
    print(fantasy_season)
    fantasy_scores = pd.concat([fantasy_scores, fantasy_season], ignore_index=True)
    time.sleep(random.randint(4,5))

print(fantasy_scores)

full_build(fantasy_scores)