def spreads(game):
    try:
        pinnacle = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 238}).get_text()
        try:
            pin_away = [float(pinnacle[:3].replace('½', '.5')), int(pinnacle[4:8])]
            pin_home = [float(pinnacle[8:12].replace('½', '.5')), int(pinnacle[-4:])]
        except ValueError:
            pin_away, pin_home = None, None
    except AttributeError:
        pin_away, pin_home = None, None
    try:
        bookmaker = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 93}).get_text()
        try:
            book_away = [float(bookmaker[:3].replace('½', '.5')), int(bookmaker[4:8])]
            book_home = [float(bookmaker[8:12].replace('½', '.5')), int(bookmaker[-4:])]
        except ValueError:
            book_away, book_home = None, None
    except AttributeError:
        book_away, book_home = None, None
    try:
        heritage = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 169}).get_text()
        try:
            her_away = [float(heritage[:3].replace('½', '.5')), int(heritage[4:8])]
            her_home = [float(heritage[8:12].replace('½', '.5')), int(heritage[-4:])]
        except ValueError:
            her_away, her_home = None, None
    except AttributeError:
        her_away, her_home = None, None
    try:
        sportsbetting = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999991}).get_text()
        try:
            sports_away = [float(sportsbetting[:3].replace('½', '.5')), int(sportsbetting[4:8])]
            sports_home = [float(sportsbetting[8:12].replace('½', '.5')), int(sportsbetting[-4:])]
        except ValueError:
            sports_away, sports_home = None, None
    except AttributeError or ValueError:
        sports_away, sports_home = None, None
    try:
        bovada = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999996}).get_text()
        try:
            bovada_away = [float(bovada[:3].replace('½', '.5')), int(bovada[4:8])]
            bovada_home = [float(bovada[8:12].replace('½', '.5')), int(bovada[-4:])]
        except ValueError:
            bovada_away, bovada_home = None, None
    except AttributeError:
        bovada_away, bovada_home = None, None

    away_odds = {'pinnacle': pin_away, 'bookmaker': book_away, 'heritage': her_away,
                 'sportsbetting': sports_away, 'bovada': bovada_away}
    home_odds = {'pinnacle': pin_home, 'bookmaker': book_home, 'heritage': her_home,
                 'sportsbetting': sports_home, 'bovada': bovada_home}

    return away_odds, home_odds
