from bs4 import BeautifulSoup
import requests
import get_moneylines as gm


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
        game_info = f'{away_team} vs {home_team}'
        line = {'game': game_info, 'away_odds': lines[0], 'home_odds': lines[1]}
        money_lines.append(line)

    return money_lines
