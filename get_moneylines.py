def moneyline(game):
    # Get lines for each site we want to scrape
    away_odds = {}
    home_odds = {}

    try:
        pinnacle = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 238}).get_text()
        try:
            away_odds['pinnacle'] = int(pinnacle[:4])
            home_odds['pinnacle'] = int(pinnacle[4:])
        except ValueError:
            pass
    except AttributeError:
        pass
    try:
        bookmaker = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 93}).get_text()
        try:
            away_odds['bookmaker'] = int(bookmaker[:4])
            home_odds['bookmaker'] = int(bookmaker[4:])
        except ValueError:
            pass
    except AttributeError:
        pass
    try:
        heritage = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 169}).get_text()
        try:
            away_odds['heritage'] = int(heritage[:4])
            home_odds['heritage'] = int(heritage[4:])
        except ValueError:
            pass
    except AttributeError:
        pass
    try:
        sportsbetting = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999991}).get_text()
        try:
            away_odds['sportsbetting'] = int(sportsbetting[:4])
            home_odds['sportsbetting'] = int(sportsbetting[4:])
        except ValueError:
            pass
    except AttributeError:
        pass
    try:
        bovada = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999996}).get_text()
        try:
            away_odds['bovada'] = int(bovada[:4])
            home_odds['bovada'] = int(bovada[4:])
        except ValueError:
            pass
    except AttributeError:
        pass

    return away_odds, home_odds
