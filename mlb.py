from bs4 import BeautifulSoup
import requests
import datetime as dt
import get_moneylines as gm


rl = 'https://classic.sportsbookreview.com/betting-odds/mlb-baseball/pointspread/'
tots = 'https://classic.sportsbookreview.com/betting-odds/mlb-baseball/totals/'


def get_game_date(game):
    """"Checks if SBR game is taking place today, yesterday, or tomorrow"""
    date = game.find('div', attrs={'class': 'date'}).get_text()
    # determine if game is today, tomorrow or past
    day = int(date.split(',')[1][-2:])
    today = dt.datetime.now().day
    if day == today:
        game_date = 'current'
    elif day - today == 1:
        game_date = 'next'
    else:
        game_date = None

    return game_date


def get_games(url):
    """Scrape MLB moneylines from SBR"""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    game_days = soup.find_all('div', attrs={'class': "eventGroup class-mlb-baseball show-rotation"})
    return game_days


def get_moneylines():
    """Scrape MLB moneylines from SBR"""
    url = 'https://classic.sportsbookreview.com/betting-odds/money-line/'
    game_days = get_games(url)

    money_lines = []

    for game_day in game_days:
        game_date = get_game_date(game_day)
        if game_date:
            games = game_day.find_all('div', attrs={'class': 'event-holder holder-scheduled'})

            for game in games:
                teams = get_game_info(game)
                game_info = f'{teams} {game_date}'
                lines = gm.moneyline(game)
                line = {'game': game_info, 'away_odds': lines[0], 'home_odds': lines[1]}
                money_lines.append(line)

    return money_lines


def get_game_info(game):
    """Get teams and time"""
    teams = game.find_all('a')
    away_team = teams[1].get_text()[:3].strip()
    home_team = teams[2].get_text()[:3].strip()
    time = game.find('div', attrs={'class': 'el-div eventLine-time'}) \
        .find('div', attrs={'class': "eventLine-book-value"}).get_text()
    return f'{away_team} vs {home_team} {time}'


def get_runlines():
    url = 'https://classic.sportsbookreview.com/betting-odds/money-line/'
    game_days = get_games(url)

    run_lines = []

    for game_day in game_days:
        game_date = get_game_date(game_day)
        if game_date:
            games = game_day.find_all('div', attrs={'class': 'event-holder holder-scheduled'})

            for game in games:
                teams = get_game_info(game)
                game_info = f'{teams} {game_date}'


mls = get_moneylines()
for ml in mls:
    print(ml)
