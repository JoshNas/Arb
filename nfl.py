from bs4 import BeautifulSoup
import requests
import get_moneylines as gm
import get_spreads as gs
import compare


def get_money_lines():
    money_lines = []

    url = 'https://classic.sportsbookreview.com/betting-odds/nfl-football/money-line/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    games = soup.find_all('div', attrs={'class': 'event-holder holder-scheduled'})

    for game in games:
        teams = game.find_all('a')
        try:
            away_team = teams[1].get_text()
            home_team = teams[2].get_text()
        except IndexError:
            # Happens when change dates. ex: gap between Sunday and Monday games
            break
        lines = gm.moneyline(game)
        if lines:
            # check that lines aren't empty
            line = {'game': f'{away_team} vs {home_team}', 'away_odds': lines[0], 'home_odds': lines[1]}
            money_lines.append(line)

    return money_lines


def get_spreads():
    spreads = []
    url = 'https://classic.sportsbookreview.com/betting-odds/nfl-football/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    games = soup.find_all('div', attrs={'class': 'event-holder holder-scheduled'})

    for game in games:
        teams = game.find_all('a')
        try:
            away_team = teams[1].get_text()
            home_team = teams[2].get_text()
        except IndexError:
            # Happens when change dates. ex: gap between Sunday and Monday games
            break
        lines = gs.spreads(game)
        if lines:
            # check that lines aren't empty
            line = {'game': f'{away_team} vs {home_team}', 'away_odds': lines[0], 'home_odds': lines[1]}
            spreads.append(line)

        return spreads
