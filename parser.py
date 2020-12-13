# AlexaWill

from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, \
    get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot
from basketball_reference_scraper.seasons import get_schedule, get_standings
from basketball_reference_scraper.box_scores import get_box_scores
from basketball_reference_scraper.shot_charts import get_shot_chart
import pandas as pd
import numpy as np

# dictionary containing all team abbreviations used by https://www.basketball-reference.com/
team_dict = {"ATLANTA HAWKS": "ATL", "ST. LOUIS HAWKS": "SLH", "MILWAUKEE HAWKS": "MIL", "TRI-CITIES BLACKHAWKS": "TCB",
             "BOSTON CELTICS": "BOS", "BROOKLYN NETS": "BRK", "NEW JERSEY NETS": "NJN", "CHICAGO BULLS": "CHI",
             "CHARLOTTE HORNETS (1988-2004)": "CHH", "CHARLOTTE HORNETS (2014-Present)": "CHO",
             "CHARLOTTE BOBCATS": "CHA", "CLEVELAND CAVALIERS": "CLE", "DALLAS MAVERICKS": "DAL",
             "DENVER NUGGETS": "DEN", "DETROIT PISTONS": "DET",
             "FORT WAYNE PISTONS": "FWP", "GOLDEN STATE WARRIORS": "GSW", "SAN FRANCISCO WARRIORS": "SFW",
             "PHILADELPHIA WARRIORS": "PHI", "HOUSTON ROCKETS": "HOU", "INDIANA PACERS": "IND",
             "LOS ANGELES CLIPPERS": "LAC", "SAN DIEGO CLIPPERS": "SDC", "BUFFALO BRAVES": "BUF",
             "LOS ANGELES LAKERS": "LAL", "MINNEAPOLIS LAKERS": "MIN", "MEMPHIS GRIZZLIES": "MEM",
             "VANCOUVER GRIZZLIES": "VAN", "MIAMI HEAT": "MIA", "MILWAUKEE BUCKS": "MIL",
             "MINNESOTA TIMBERWOLVES": "MIN", "NEW ORLEANS PELICANS": "NOP", "NEW ORLEANS/OKLAHOMA CITY HORNETS": "NOK",
             "NEW ORLEANS HORNETS": "NOH", "NEW YORK KNICKS": "NYK", "OKLAHOMA CITY THUNDER": "OKC",
             "SEATTLE SUPERSONICS": "SEA", "ORLANDO MAGIC": "ORL", "PHILADELPHIA 76ERS": "PHI",
             "SYRACUSE NATIONALS": "SYR", "PHOENIX SUNS": "PHO", "PORTLAND TRAIL BLAZERS": "POR",
             "SACRAMENTO KINGS": "SAC", "KANSAS CITY KINGS": "KCK", "KANSAS CITY-OMAHA KINGS": "KCK",
             "CINCINNATI ROYALS": "CIN", "ROCHESTER ROYALS": "ROR", "SAN ANTONIO SPURS": "SAS",
             "TORONTO RAPTORS": "TOR", "UTAH JAZZ": "UTA", "NEW ORLEANS JAZZ": "NOJ", "WASHINGTON WIZARDS": "WAS",
             "WASHINGTON BULLETS": "WAS", "CAPITAL BULLETS": "CAP", "BALTIMORE BULLETS": "BAL",
             "CHICAGO ZEPHYRS": "CHI", "CHICAGO PACKERS": "CHI", "ANDERSON PACKERS": "AND", "CHICAGO STAGS": "CHI",
             "INDIANAPOLIS OLYMPIANS": "IND", "SHEBOYGAN RED SKINS": "SRS", "ST. LOUIS BOMBERS": "SLB",
             "WASHINGTON CAPITOLS": "WAS", "WATERLOO HAWKS": "WAT"}

team_stats = pd.DataFrame(
    columns=['G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB',
             'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'TEAM', 'SEASON'])

opp_stats = pd.DataFrame(
    columns=['OPP_G', 'OPP_MP', 'OPP_FG', 'OPP_FGA', 'OPP_FG%', 'OPP_3P', 'OPP_3PA', 'OPP_3P%', 'OPP_2P', 'OPP_2PA',
             'OPP_2P%', 'OPP_FT', 'OPP_FTA', 'OPP_FT%', 'OPP_ORB', 'OPP_DRB', 'OPP_TRB', 'OPP_AST', 'OPP_STL',
             'OPP_BLK', 'OPP_TOV', 'OPP_PF', 'OPP_PTS', 'TEAM', 'SEASON'])

for i in range(2011, 2021):
    # this section is to only get abbreviations for teams that are active for a specific season. Without this we get and indexing error
    schedule = get_schedule(i, playoffs=False)
    schedule = list(dict.fromkeys(schedule['HOME'].values.tolist()))
    schedule = [x.upper() for x in schedule]

    # intersection of active teams and teams in dictionary
    keys = team_dict.keys() & schedule
    team_abbr = [team_dict[x] for x in keys]

    # populating the team_stats, opp_stats dataframes with data from active teams and desired date range
    for team in team_abbr:
        temp = get_team_stats(team, i, 'TOTAL').to_frame().T  # transposing temp table
        team_stats = team_stats.append(temp, ignore_index=True)

        temp1 = get_opp_stats(team, i, 'TOTAL').to_frame().T
        opp_stats = opp_stats.append(temp1, ignore_index=True)

# Export dataframes to CSV for analysis/cleaning
team_stats.to_csv('team_stats.csv', index=False)
opp_stats.to_csv('opp_stats.csv', index=False)
