
def run_lines(game):
    away_odds = {}
    home_odds = {}

    try:
        pinnacle = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 238}).get_text()
        away, home = extract_runlines(pinnacle)
        if away:
            away_odds['pinnacle'], home_odds['pinnacle'] = away, home
    except AttributeError:
        pass
    try:
        bookmaker = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 93}).get_text()
        away, home = extract_runlines(bookmaker)
        if away:
            away_odds['bookmaker'], home_odds['bookmaker'] = away, home
    except AttributeError:
        pass
    try:
        heritage = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 169}).get_text()
        away, home = extract_runlines(heritage)
        if away:
            away_odds['heritage'], home_odds['heritage'] = away, home
    except AttributeError:
        pass
    try:
        sportsbetting = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999991}).get_text()
        away, home = extract_runlines(sportsbetting)
        if away:
            away_odds['sportsbetting'], home_odds['sportsbetting'] = away, home
    except AttributeError or ValueError:
        pass
    try:
        bovada = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999996}).get_text()
        away, home = extract_runlines(bovada)
        if away:
            away_odds['bovada'], home_odds['bovada'] = away, home
    except AttributeError:
        pass

    return away_odds, home_odds


def extract_runlines(site):
    try:
        away_odds = [float(site[:3].replace('½', '.5')), int(site[4:8])]
        home_odds = [float(site[8:12].replace('½', '.5')), int(site[-4:])]
    except ValueError:
        return None, None
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
            away_odds['heritage'], home_odds['heritage'] = away_line, home_line
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
    except (TypeError, ValueError):
        return None, None
    return away_line, home_line
