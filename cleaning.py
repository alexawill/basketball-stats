import pandas as pd
import numpy as np

team_stats = pd.read_csv('team_stats.csv')
team_stats['SEASON_START'] = team_stats['SEASON'].str.split('-').str[0].astype('int64')
team_stats.to_csv('team_stats.csv', index=False)


opp_stats = pd.read_csv('opp_stats.csv')
opp_stats['SEASON_START'] = opp_stats['SEASON'].str.split('-').str[0].astype('int64')
opp_stats.to_csv('opp_stats.csv', index=False)
