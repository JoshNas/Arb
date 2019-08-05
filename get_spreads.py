def run_lines(game):
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


def spreads(game):
    away_odds = {}
    home_odds = {}
    try:
        pinnacle = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 238}).get_text()\
            .replace('PK', '0 ').replace('\xa0', ' ').replace('½', '.5').split(' ')
        away_line, home_line = extract_spreads(pinnacle)
        if away_line:
            away_odds['pinnacle'], home_odds['pinnacle'] = away_line, home_line
    except AttributeError:
        pass

    try:
        bookmaker = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 93}).get_text()\
            .replace('PK', '0 ').replace('\xa0', ' ').replace('½', '.5').split(' ')
        away_line, home_line = extract_spreads(bookmaker)
        if away_line:
            away_odds['bookmaker'], home_odds['bookmaker'] = away_line, home_line
    except AttributeError:
        pass

    try:
        heritage = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 169}).get_text()\
            .replace('PK', '0 ').replace('\xa0', ' ').replace('½', '.5').split(' ')
        away_line, home_line = extract_spreads(heritage)
        if away_line:
            away_odds['heritage'],home_odds['heritage'] = away_line, home_line
    except AttributeError:
        pass

    try:
        sportsbetting = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999991}).get_text()\
            .replace('PK', '0 ').replace('\xa0', ' ').replace('½', '.5').split(' ')
        away_line, home_line = extract_spreads(sportsbetting)
        if away_line:
            away_odds['sportsbetting'], home_odds['sportsbetting'] = away_line, home_line
    except AttributeError:
        pass

    try:
        bovada = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999996}).get_text()\
            .replace('PK', '0 ').replace('\xa0', ' ').replace('½', '.5').split(' ')
        away_line, home_line = extract_spreads(bovada)
        if away_line:
            away_odds['bovada'], home_odds['bovada'] = away_line, home_line
    except AttributeError:
        pass

    return away_odds, home_odds


def extract_spreads(site):
    try:
        away_line = [float(site[0]), int(site[1][:4])]
        home_line = [float(site[1][4:]), int(site[2])]
    except TypeError:
        return None
    return away_line, home_line
