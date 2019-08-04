def moneyline(game):
    # Get lines for each site we want to scrape
    try:
        pinnacle = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 238}).get_text()
        try:
            pin_away = int(pinnacle[:4])
            pin_home = int(pinnacle[4:])
        except ValueError:
            pin_away, pin_home = None, None
    except AttributeError:
        pin_away, pin_home = None, None
    try:
        bookmaker = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 93}).get_text()
        try:
            book_away = int(bookmaker[:4])
            book_home = int(bookmaker[4:])
        except ValueError:
            book_away, book_home = None, None
    except AttributeError:
        book_away, book_home = None, None
    try:
        heritage = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 169}).get_text()
        try:
            her_away = int(heritage[:4])
            her_home = int(heritage[4:])
        except ValueError:
            her_away, her_home = None, None
    except AttributeError:
        her_away, her_home = None, None
    try:
        sportsbetting = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999991}).get_text()
        try:
            sports_away = int(sportsbetting[:4])
            sports_home = int(sportsbetting[4:])
        except ValueError:
            sports_away, sports_home = None, None
    except AttributeError:
        sports_away, sports_home = None, None
    try:
        bovada = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999996}).get_text()
        try:
            bovada_away = int(bovada[:4])
            bovada_home = int(bovada[4:])
        except ValueError:
            bovada_away, bovada_home = None, None
    except AttributeError:
        bovada_away, bovada_home = None, None

    away_odds = {'pinnacle': pin_away, 'bookmaker': book_away, 'heritage': her_away,
                 'sportsbetting': sports_away, 'bovada': bovada_away}
    home_odds = {'pinnacle': pin_home, 'bookmaker': book_home, 'heritage': her_home,
                 'sportsbetting': sports_home, 'bovada': bovada_home}

    return away_odds, home_odds
