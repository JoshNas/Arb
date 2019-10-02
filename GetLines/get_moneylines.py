import re


def moneyline(game):
    # Get lines for each site we want to scrape
    away_odds = {}
    home_odds = {}

    try:
        pinnacle = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 238}).get_text()
        away, home = clean(pinnacle)
        if away:
            away_odds['pinnacle'] = away
            home_odds['pinnacle'] = home
    except AttributeError:
        pass

    try:
        bookmaker = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 93}).get_text()
        away, home = clean(bookmaker)
        if away:
            away_odds['bookmaker'] = away
            home_odds['bookmaker'] = home
    except AttributeError:
        pass

    try:
        heritage = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 169}).get_text()
        away, home = clean(heritage)
        if away:
            away_odds['heritage'] = away
            home_odds['heritage'] = home
    except AttributeError:
        pass

    try:
        sportsbetting = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999991}).get_text()
        away, home = clean(sportsbetting)
        if away:
            away_odds['sportsbetting'] = away
            home_odds['sportsbetting'] = home
    except AttributeError:
        pass

    try:
        bovada = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999996}).get_text()
        away, home = clean(bovada)
        if away:
            away_odds['bovada'] = away
            home_odds['bovada'] = home
    except AttributeError:
        pass

    return away_odds, home_odds


def clean(site):
    """Splits site odds in first non-numeric character and converts to int. Checks if first value is positive or
    negative and assign opposite to second value

    Parameters:
    site (str): '+130-145'

    Returns:
    ints: 130, -145

    """
    negatives = site.count('-')  # find out if both home and away or negative before splitting
    odds = re.split(r'(?<=\d)\D', site)

    try:
        away = int(odds[0])
        home = int(odds[1])
        if negatives == 2 or away > 0:
            # convert home odds after losing sign on split
            home = home * -1
        return away, home
    except (ValueError, IndexError):
        # no odds for this site
        return None, None
