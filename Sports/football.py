from bs4 import BeautifulSoup
import requests
from GetLines import get_totals as gt, get_moneylines as gm, get_spreads as gs


def get_money_lines(url):
    games = get_games(url)
    money_lines = []

    for game in games:
        away_team, home_team = get_teams(game)
        if away_team:
            lines = gm.moneyline(game)
            if lines:
                # check that lines aren't empty
                line = {'game': f'{away_team} vs {home_team}', 'away_odds': lines[0], 'home_odds': lines[1]}
                money_lines.append(line)

    return money_lines


def get_spreads(url):
    games = get_games(url)
    spreads = []

    for game in games:
        away_team, home_team = get_teams(game)
        if away_team:
            lines = gs.spreads(game)
            if lines:
                line = {'game': f'{away_team} vs {home_team}', 'away_odds': lines[0], 'home_odds': lines[1]}
                spreads.append(line)

    return spreads


def get_totals(url):
    games = get_games(url)
    totals = []

    for game in games:
        away_team, home_team = get_teams(game)
        if away_team:
            total = gt.totals(game)
            if total:
                line = {'game': f'{away_team} vs {home_team}', 'overs': total[0], 'unders': total[1]}
                totals.append(line)
    return totals


def get_games(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('div', attrs={'class': 'event-holder holder-scheduled'})


def get_teams(game):
    teams = game.find_all('a')
    try:
        away_team = teams[1].get_text()
        home_team = teams[2].get_text()
    except IndexError:
        # Happens when change dates. ex: gap between Sunday and Monday games
        return None
    return away_team, home_team
