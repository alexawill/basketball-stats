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
        stats = [[td.getText() for td in rows[x].findAll('td')]
                 for x in range(len(rows))]

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
        stats = [[td.getText() for td in rows[x].findAll('td')]
                 for x in range(len(rows))]

        temp = pd.DataFrame(stats, columns=headers)
        temp['Season'] = f"{i - 1}-{i}"
        df = df.append(temp)

    df.dropna(inplace=True)
    return df


def getSeasonStandings(startyear, endyear):
    dfEast = pd.DataFrame()
    dfWest = pd.DataFrame()

    for i in range(startyear, endyear + 1):
        # Eastern conference url
        url = f"https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{i}.html&div=div_confs_standings_E"

        html = urlopen(url)
        soup = BeautifulSoup(html, features="html.parser")

        # use findALL() to get the column headers
        soup.findAll('tr', limit=2)

        # use getText()to extract the text we need into a list
        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

        # avoid the first header row
        rows = soup.findAll('tr')[1:]

        stats = [[td.getText() for td in rows[x].findAll(['a', 'td'])]
                 for x in range(len(rows))]

        temp = pd.DataFrame(stats, columns=headers)
        temp.rename(columns={"Eastern Conference": "Team"}, inplace=True)
        temp['Season'] = f"{i - 1}-{i}"
        temp['Conference'] = "East"
        dfEast = dfEast.append(temp)

    for i in range(startyear, endyear + 1):
        # Western conference url
        url = f"https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{i}.html&div=div_confs_standings_W"

        html = urlopen(url)
        soup = BeautifulSoup(html, features="html.parser")

        # use findALL() to get the column headers
        soup.findAll('tr', limit=2)

        # use getText()to extract the text we need into a list
        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

        # avoid the first header row
        rows = soup.findAll('tr')[1:]

        stats = [[td.getText() for td in rows[x].findAll(['a', 'td'])]
                 for x in range(len(rows))]

        temp = pd.DataFrame(stats, columns=headers)
        temp.rename(columns={"Western Conference": "Team"}, inplace=True)
        temp['Season'] = f"{i - 1}-{i}"
        temp['Conference'] = "West"
        dfWest = dfWest.append(temp)

    df = dfEast.append(dfWest).convert_dtypes()
    df['GB'] = df['GB'].apply(lambda x: x.replace('—', '0'))

    return df
