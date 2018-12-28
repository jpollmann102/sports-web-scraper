import sys
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains as AC
from bs4 import BeautifulSoup as BS

# team offense @ http://www.espn.com/nfl/statistics/team/_/stat/total
# team defense @ http://www.espn.com/nfl/statistics/team/_/stat/total/position/defense
def scrapeNFLTeamStats(offense=True):
    if offense:
        url = 'http://www.espn.com/nfl/statistics/team/_/stat/total'
        outFileName = 'data/nfl/nfl_team_offense.csv'
    else:
        url = 'http://www.espn.com/nfl/statistics/team/_/stat/total/position/defense'
        outFileName = 'data/nfl/nfl_team_defense.csv'

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=options)

    try:
        driver.set_page_load_timeout(60)
        driver.get(url)
        wait = WebDriverWait(driver, 100)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tablehead')))
        html = driver.page_source

    except TimeoutException as ex:
        isrunning = 0
        print(str(ex))
        driver.close()
        sys.exit()

    driver.quit()

    soup = BS(html, 'html.parser')
    teamOTable = soup.find_all('table')[0]
    names = ['Rank','Tm', 'Yds', 'Yds/G', 'PYds', 'PYds/G', 'RYds', 'RYds/G', 'PTS', 'PTS/G']
    table = pd.DataFrame(columns=names, index=range(0,32))
    rows = teamOTable.find_all('tr')

    rowMarker = 0
    for i in range(1,len(rows)):
        colMarker = 0
        columns = rows[i].find_all('td')
        for column in columns:
            table.iat[rowMarker, colMarker] = column.get_text()
            colMarker += 1
        rowMarker += 1

    table.sort_values(by=['Tm'], inplace=True)
    table.drop('Rank', axis=1, inplace=True)
    table.to_csv(outFileName, index_label=False)

# team passing @ http://www.espn.com/nfl/statistics/team/_/stat/passing
# team pass D @ http://www.espn.com/nfl/statistics/team/_/stat/passing/position/defense
def scrapeNFLPassingStats(offense=True):
    if offense:
        url = 'http://www.espn.com/nfl/statistics/team/_/stat/passing'
        outFileName = 'data/nfl/nfl_team_pass_offense.csv'
    else:
        url = 'http://www.espn.com/nfl/statistics/team/_/stat/passing/position/defense'
        outFileName = 'data/nfl/nfl_team_pass_defense.csv'

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=options)

    try:
        driver.set_page_load_timeout(60)
        driver.get(url)
        wait = WebDriverWait(driver, 100)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tablehead')))
        html = driver.page_source

    except TimeoutException as ex:
        isrunning = 0
        print(str(ex))
        driver.close()
        sys.exit()

    driver.quit()

    soup = BS(html, 'html.parser')
    teamOTable = soup.find_all('table')[0]
    names = ['Rank','Tm', 'Attempts', 'Completions', 'Percentage', 'Yds', 'Yds/A', 'Long', 'TD', 'Int', 'Sacks', 'YdsL', 'Passer Rating', 'Yds/G']
    table = pd.DataFrame(columns=names, index=range(0,32))
    rows = teamOTable.find_all('tr')

    rowMarker = 0
    for i in range(1,len(rows)):
        colMarker = 0
        columns = rows[i].find_all('td')
        for column in columns:
            table.iat[rowMarker, colMarker] = column.get_text()
            colMarker += 1
        rowMarker += 1

    table.sort_values(by=['Tm'], inplace=True)
    table.drop(['Rank','Attempts','Completions','Long','Sacks','YdsL'], axis=1, inplace=True)
    table.to_csv(outFileName, index_label=False)

# team rushing @ http://www.espn.com/nfl/statistics/team/_/stat/rushing
# team rush D @ http://www.espn.com/nfl/statistics/team/_/stat/rushing/position/defense
def scrapeNFLRushingStats(offense=True):
    if offense:
        url = 'http://www.espn.com/nfl/statistics/team/_/stat/rushing'
        outFileName = 'data/nfl/nfl_team_rush_offense.csv'
    else:
        url = 'http://www.espn.com/nfl/statistics/team/_/stat/rushing/position/defense'
        outFileName = 'data/nfl/nfl_team_rush_defense.csv'

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=options)

    try:
        driver.set_page_load_timeout(60)
        driver.get(url)
        wait = WebDriverWait(driver, 100)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tablehead')))
        html = driver.page_source

    except TimeoutException as ex:
        isrunning = 0
        print(str(ex))
        driver.close()
        sys.exit()

    driver.quit()

    soup = BS(html, 'html.parser')
    teamOTable = soup.find_all('table')[0]
    names = ['Rank','Tm', 'Attempts', 'Yds', 'Yds/A', 'Long', 'TD', 'Yds/G', 'Fumbles', 'FumL']
    table = pd.DataFrame(columns=names, index=range(0,32))
    rows = teamOTable.find_all('tr')

    rowMarker = 0
    for i in range(1,len(rows)):
        colMarker = 0
        columns = rows[i].find_all('td')
        for column in columns:
            table.iat[rowMarker, colMarker] = column.get_text()
            colMarker += 1
        rowMarker += 1

    table.sort_values(by=['Tm'], inplace=True)
    table.drop(['Rank','Attempts','Long','Fumbles','FumL'], axis=1, inplace=True)
    table.to_csv(outFileName, index_label=False)

# team receiving @ http://www.espn.com/nfl/statistics/team/_/stat/receiving
# team receiving D @ http://www.espn.com/nfl/statistics/team/_/stat/receiving/position/defense
def scrapeNFLReceivingStats(offense=True):
    if offense:
        url = 'http://www.espn.com/nfl/statistics/team/_/stat/receiving'
        outFileName = 'data/nfl/nfl_team_receiving_offense.csv'
    else:
        url = 'http://www.espn.com/nfl/statistics/team/_/stat/receiving/position/defense'
        outFileName = 'data/nfl/nfl_team_receiving_defense.csv'

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=options)

    try:
        driver.set_page_load_timeout(60)
        driver.get(url)
        wait = WebDriverWait(driver, 100)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tablehead')))
        html = driver.page_source

    except TimeoutException as ex:
        isrunning = 0
        print(str(ex))
        driver.close()
        sys.exit()

    driver.quit()

    soup = BS(html, 'html.parser')
    teamOTable = soup.find_all('table')[0]
    names = ['Rank','Tm', 'Receptions', 'Yds', 'Average', 'Long', 'TD', 'Yds/G', 'Fumbles', 'FumL']
    table = pd.DataFrame(columns=names, index=range(0,32))
    rows = teamOTable.find_all('tr')

    rowMarker = 0
    for i in range(1,len(rows)):
        colMarker = 0
        columns = rows[i].find_all('td')
        for column in columns:
            table.iat[rowMarker, colMarker] = column.get_text()
            colMarker += 1
        rowMarker += 1

    table.sort_values(by=['Tm'], inplace=True)
    table.drop(['Rank','Receptions','Long','Fumbles','FumL'], axis=1, inplace=True)
    table.to_csv(outFileName, index_label=False)

# team offense @ http://www.espn.com/nba/statistics/team/_/stat/offense-per-game
# team defense @ http://www.espn.com/nba/statistics/team/_/stat/defense-per-game
def scrapeNBATeamStats(offense=True):
    if offense:
        url = 'http://www.espn.com/nba/statistics/team/_/stat/offense-per-game'
        outFileName = 'data/nba/nba_team_offense.csv'
    else:
        url = 'http://www.espn.com/nba/statistics/team/_/stat/defense-per-game'
        outFileName = 'data/nba/nba_team_defense.csv'

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=options)

    try:
        driver.set_page_load_timeout(60)
        driver.get(url)
        wait = WebDriverWait(driver, 100)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tablehead')))
        html = driver.page_source

    except TimeoutException as ex:
        isrunning = 0
        print(str(ex))
        driver.close()
        sys.exit()

    driver.quit()

    soup = BS(html, 'html.parser')
    teamOTable = soup.find_all('table')[0]
    names = ['Rank','Tm', 'Points', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'PPS', 'AFG%']
    table = pd.DataFrame(columns=names, index=range(0,30))
    rows = teamOTable.find_all('tr')

    rowMarker = 0
    for i in range(1, len(rows)):
        if i % 11 == 0:
            continue
        colMarker = 0
        columns = rows[i].find_all('td')
        for column in columns:
            table.iat[rowMarker, colMarker] = column.get_text()
            colMarker += 1
        rowMarker += 1

    table.sort_values(by=['Tm'], inplace=True)
    table.drop(['Rank','Points','FGA','FGM','3PA','3PM','FTM'], axis=1, inplace=True)
    table.to_csv(outFileName, index_label=False)

# team rebounds @ http://www.espn.com/nba/statistics/team/_/stat/rebounds-per-game
def scrapeNBATeamReboundStats():

    url = 'http://www.espn.com/nba/statistics/team/_/stat/rebounds-per-game'
    outFileName = 'data/nba/nba_team_rebounds.csv'

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=options)

    try:
        driver.set_page_load_timeout(60)
        driver.get(url)
        wait = WebDriverWait(driver, 100)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tablehead')))
        html = driver.page_source

    except TimeoutException as ex:
        isrunning = 0
        print(str(ex))
        driver.close()
        sys.exit()

    driver.quit()

    soup = BS(html, 'html.parser')
    teamOTable = soup.find_all('table')[0]
    names = ['Rank','Tm', 'OFF%', 'DEF%', 'REB%', 'ORPG', 'OppORPG', 'DRPG', 'OppDRPG', 'RPG', 'OppRPG', 'Diff']
    table = pd.DataFrame(columns=names, index=range(0,30))
    rows = teamOTable.find_all('tr')

    rowMarker = 0
    for i in range(2,len(rows)):
        if i == 13:
            continue
        if i == 25:
            continue
        if i % 12 == 0:
            continue
        colMarker = 0
        columns = rows[i].find_all('td')
        for column in columns:
            table.iat[rowMarker, colMarker] = column.get_text()
            colMarker += 1
        rowMarker += 1

    table.sort_values(by=['Tm'], inplace=True)
    table.drop(['Rank','OFF%','DEF%','REB%'], axis=1, inplace=True)
    table.to_csv(outFileName, index_label=False)

# scrape all NFL stats
def scrapeAllNFL():
    scrapeNFLTeamStats(offense=True)
    scrapeNFLTeamStats(offense=False)
    scrapeNFLPassingStats(offense=True)
    scrapeNFLPassingStats(offense=False)
    scrapeNFLRushingStats(offense=True)
    scrapeNFLRushingStats(offense=False)
    scrapeNFLReceivingStats(offense=True)
    scrapeNFLReceivingStats(offense=False)

# scrape all NBA stats
def scrapeAllNBA():
    scrapeNBATeamStats(offense=True)
    scrapeNBATeamStats(offense=False)
    scrapeNBATeamReboundStats()
