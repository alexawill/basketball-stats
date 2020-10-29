# AlexaWill
# References:
#

from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, \
    get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot
from basketball_reference_scraper.seasons import get_schedule, get_standings
from basketball_reference_scraper.box_scores import get_box_scores
import pandas as pd

team_abbr = {"ATLANTA HAWKS": "ATL", "ST. LOUIS HAWKS": "SLH", "MILWAUKEE HAWKS": "MIL", "TRI-CITIES BLACKHAWKS": "TCB",
             "BOSTON CELTICS": "BOS", "BROOKLYN NETS": "BRK", "NEW JERSEY NETS": "NJN", "CHICAGO BULLS": "CHI",
             "CHARLOTTE HORNETS (1988-2004)": "CHH", "CHARLOTTE HORNETS (2014-Present)": "CHO", "CHARLOTTE BOBCATS": "CHA",
             "CLEVELAND CAVALIERS": "CLE", "DALLAS MAVERICKS": "DAL", "DENVER NUGGETS": "DEN", "DETROIT PISTONS": "DET",
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
