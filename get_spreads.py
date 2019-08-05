def spreads(game):
    away_odds = {}
    home_odds = {}

    try:
        pinnacle = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 238}).get_text()
        try:
            away_odds['pinnacle'] = [float(pinnacle[:3].replace('½', '.5')), int(pinnacle[4:8])]
            home_odds['pinnacle'] = [float(pinnacle[8:12].replace('½', '.5')), int(pinnacle[-4:])]
        except ValueError:
            pass
    except AttributeError:
        pass
    try:
        bookmaker = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 93}).get_text()
        try:
            away_odds['bookmaker'] = [float(bookmaker[:3].replace('½', '.5')), int(bookmaker[4:8])]
            home_odds['bookmaker'] = [float(bookmaker[8:12].replace('½', '.5')), int(bookmaker[-4:])]
        except ValueError:
            pass
    except AttributeError:
        pass
    try:
        heritage = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 169}).get_text()
        try:
            away_odds['heritage'] = [float(heritage[:3].replace('½', '.5')), int(heritage[4:8])]
            home_odds['heritage'] = [float(heritage[8:12].replace('½', '.5')), int(heritage[-4:])]
        except ValueError:
            pass
    except AttributeError:
        pass
    try:
        sportsbetting = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999991}).get_text()
        try:
            away_odds['sportsbetting'] = [float(sportsbetting[:3].replace('½', '.5')), int(sportsbetting[4:8])]
            home_odds['sportsbetting'] = [float(sportsbetting[8:12].replace('½', '.5')), int(sportsbetting[-4:])]
        except ValueError:
            pass
    except AttributeError or ValueError:
        pass
    try:
        bovada = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999996}).get_text()
        try:
            away_odds['bovada'] = [float(bovada[:3].replace('½', '.5')), int(bovada[4:8])]
            home_odds['bovada'] = [float(bovada[8:12].replace('½', '.5')), int(bovada[-4:])]
        except ValueError:
            pass
    except AttributeError:
        pass

    return away_odds, home_odds
