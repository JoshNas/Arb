def totals(game):
    pinnacle = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 238}).get_text()
    bookmaker = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 93}).get_text()
    heritage = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 169}).get_text()
    sportsbetting = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999991}).get_text()
    bovada = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999996}).get_text()

    if len(pinnacle) == 14:
        # for lines with 1/2 or double digits
        pin_over = [float(pinnacle[0:2].replace('½', '.5')), fix_neg(int(pinnacle[3:7]))]
        pin_under = [float(pinnacle[0:2].replace('½', '.5')), fix_neg(int(pinnacle[-4:]))]
    elif len(pinnacle) == 12:
        pin_over = [float(pinnacle[0]), fix_neg(int(pinnacle[2:6]))]
        pin_under = [float(pinnacle[0]), fix_neg(int(pinnacle[-4:]))]
    elif len(pinnacle) == 16:
        # for lines with 1/2 and double digits
        pin_over = [float(pinnacle[0:3].replace('½', '.5')), fix_neg(int(pinnacle[4:7]))]
        pin_under = [float(pinnacle[0:3].replace('½', '.5')), fix_neg(int(pinnacle[-4:]))]

    else:
        # total is repeated twice so should always be either 14 or 12 if exists
        pin_over = ''
        pin_under = ''

    if len(bookmaker) == 14:
        book_over = [float(bookmaker[0:2].replace('½', '.5')), int(bookmaker[3:7])]
        book_under = [float(bookmaker[0:2].replace('½', '.5')), int(bookmaker[-4:])]
    elif len(bookmaker) == 12:
        book_over = [float(bookmaker[0]), int(bookmaker[2:6])]
        book_under = [float(bookmaker[0]), int(bookmaker[-4:])]
    elif len(bookmaker) == 16:
        book_over = [float(bookmaker[0:3].replace('½', '.5')), int(bookmaker[4:7])]
        book_under = [float(bookmaker[0:3].replace('½', '.5')), int(bookmaker[-4:])]
    else:
        # total is repeated twice so should always be either 14 or 12 if exists
        book_over = ''
        book_under = ''

    if len(heritage) == 14:
        her_over = [float(heritage[0:2].replace('½', '.5')), int(heritage[3:7])]
        her_under = [float(heritage[0:2].replace('½', '.5')), int(heritage[-4:])]
    elif len(heritage) == 12:
        her_over = [float(heritage[0]), int(heritage[2:6])]
        her_under = [float(heritage[0]), int(heritage[-4:])]
    elif len(heritage) == 16:
        her_over = [float(heritage[0:3].replace('½', '.5')), int(heritage[4:7])]
        her_under = [float(heritage[0:3].replace('½', '.5')), int(heritage[-4:])]
    else:
        # total is repeated twice so should always be either 14 or 12 if exists
        her_over = ''
        her_under = ''

    if len(sportsbetting) == 14:
        sports_over = [float(sportsbetting[0:2].replace('½', '.5')), int(sportsbetting[3:7])]
        sports_under = [float(sportsbetting[0:2].replace('½', '.5')), int(sportsbetting[-4:])]
    elif len(sportsbetting) == 12:
        sports_over = [float(sportsbetting[0]), int(sportsbetting[2:6])]
        sports_under = [float(sportsbetting[0]), int(sportsbetting[-4:])]
    elif len(sportsbetting) == 16:
        sports_over = [float(sportsbetting[0:3].replace('½', '.5')), int(sportsbetting[4:7])]
        sports_under = [float(sportsbetting[0:3].replace('½', '.5')), int(sportsbetting[-4:])]
    else:
        # total is repeated twice so should always be either 14 or 12 if exists
        sports_over = ''
        sports_under = ''

    if len(bovada) == 14:
        bovada_over = [float(bovada[0:2].replace('½', '.5')), int(bovada[3:7])]
        bovada_under = [float(bovada[0:2].replace('½', '.5')), int(bovada[-4:])]
    elif len(bovada) == 12:
        bovada_over = [float(bovada[0]), int(bovada[2:6])]
        bovada_under = [float(bovada[0]), int(bovada[-4:])]
    elif len(bovada) == 16:
        bovada_over = [float(bovada[0:3].replace('½', '.5')), int(bovada[4:7])]
        bovada_under = [float(bovada[0:3].replace('½', '.5')), int(bovada[-4:])]
    else:
        # total is repeated twice so should always be either 14 or 12 if exists
        bovada_over = ''
        bovada_under = ''

    over_odds = {'pinnacle': pin_over, 'bookmaker': book_over, 'heritage': her_over,
                 'sportsbetting': sports_over, 'bovada': bovada_over}
    under_odds = {'pinnacle': pin_under, 'bookmaker': book_under, 'heritage': her_under,
                  'sportsbetting': sports_under, 'bovada': bovada_under}

    return over_odds, under_odds


def fix_neg(odds):
    """Sometimes even odds are displayed as -100"""
    if odds == -100:
        return 100
    else:
        return odds
