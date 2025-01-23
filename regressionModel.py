import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import sqlalchemy
from seaborn import pairplot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

conn = sqlite3.connect('playerDatabase.sqlite')

df = pd.read_sql_query("SELECT * FROM completeStats", conn)
rb = pd.read_sql_query("SELECT * FROM completeStats WHERE position = 'RB'", conn)
wr = pd.read_sql_query("SELECT * FROM completeStats WHERE position = 'WR'", conn)
qb = pd.read_sql_query("SELECT * FROM completeStats WHERE position = 'QB'", conn)
fb = pd.read_sql_query("SELECT * FROM completeStats WHERE position = 'FB'", conn)
te = pd.read_sql_query("SELECT * FROM completeStats WHERE position = 'TE'", conn)

df_array = [df, rb, wr, qb, fb, te]
print(df.describe())
i = 0
strings = ['Total Data', 'RB', 'WR', 'QB', 'FB', 'TE']
for df_item in df_array:
    i += 1
    if 1 <= i <= len(strings):
        string = strings[i-1]

    X = df_item[['age', 'prev_games_played', 'prev_games_started', 'prev_passing_completions', 'prev_passing_attempts', \
            'prev_passing_yards', 'prev_passing_TDs', 'prev_interceptions', 'prev_rushing_attempts', 'prev_rushing_yards', \
            'prev_yards_per_attempt', 'prev_rushing_TDs', 'prev_targets', 'prev_receptions', 'prev_receiving_yards', 'prev_yards_per_reception', \
            'prev_receiving_TDs', 'prev_fumbles', 'prev_fumbles_lost', 'prev_two_point_conversions', 'prev_two_point_passes', 'prev_fantasy_points']]
    y = df_item['fantasy_points']


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    lm = LinearRegression()
    lm.fit(X_train, y_train)
    print(lm.coef_)
    predictions = lm.predict(X_test)
    print(predictions)
    sns.scatterplot(x=predictions, y=y_test, alpha=0.3)
    plt.xlabel('Predictions')
    plt.ylabel('Actual')
    plt.title('Evaluation of LM model for ' + string )
    plt.show()
