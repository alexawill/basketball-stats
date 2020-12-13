from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def getTeamStats(startyear, endyear):
    df = pd.DataFrame()

    for i in range(startyear, endyear + 1):
        url = f"https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{i}.html&div=div_team-stats-base"

        html = urlopen(url)
        soup = BeautifulSoup(html, features="html.parser")

        # use findALL() to get the column headers
        soup.findAll('tr', limit=2)

        # use getText()to extract the text we need into a list
        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

        # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
        headers = headers[1:]

        # avoid the first header row
        rows = soup.findAll('tr')[1:]
        stats = [[td.getText() for td in rows[i].findAll('td')]
                 for i in range(len(rows))]

        temp = pd.DataFrame(stats, columns=headers)
        temp['Season'] = f"{i - 1}-{i}"
        df = df.append(temp)

    df['Team'] = df['Team'].apply(lambda x: x.replace('*', '').upper())
    df = df[df.Team != 'LEAGUE AVERAGE']

    return df


def getPlayerStats(startyear, endyear):
    df = pd.DataFrame()

    for i in range(startyear, endyear + 1):
        url = f"https://www.basketball-reference.com/leagues/NBA_{i}_per_game.html"

        html = urlopen(url)
        soup = BeautifulSoup(html, features="html.parser")

        # use findALL() to get the column headers
        soup.findAll('tr', limit=2)

        # use getText()to extract the text we need into a list
        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

        # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
        headers = headers[1:]

        # avoid the first header row
        rows = soup.findAll('tr')[1:]
        stats = [[td.getText() for td in rows[i].findAll('td')]
                 for i in range(len(rows))]

        temp = pd.DataFrame(stats, columns=headers)
        temp['Season'] = f"{i - 1}-{i}"
        df = df.append(temp)

    df.dropna(inplace=True)
    return df
