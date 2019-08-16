def totals(game):
    overs = {}
    unders = {}

    try:
        pinnacle = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 238}).get_text()
        over, under = get_site(pinnacle)
        if over:
            overs['pinnacle'] = over
            unders['pinnacle'] = under
    except AttributeError:
        pass

    try:
        bookmaker = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 93}).get_text()
        over, under = get_site(bookmaker)
        if over:
            overs['bookmaker'] = over
            unders['bookmaker'] = under
    except AttributeError:
        pass

    try:
        heritage = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 169}).get_text()
        over, under = get_site(heritage)
        if over:
            overs['heritage'] = over
            unders['heritage'] = under
    except AttributeError:
        pass

    try:
        sportsbetting = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999991}).get_text()
        over, under = get_site(sportsbetting)
        if over:
            overs['sportsbetting'] = over
            unders['sportsbetting'] = under
    except AttributeError:
        pass

    try:
        bovada = game.find('div', attrs={'class': 'el-div eventLine-book', 'rel': 999996}).get_text()
        over, under = get_site(bovada)
        if over:
            overs['bovada'] = over
            unders['bovada'] = under
    except AttributeError:
        pass

    return overs, unders


def get_site(odds):
    """Pass in odds"""
    if len(odds) == 14:
        # for lines with 1/2 or double digits
        over = [float(odds[0:2].replace('½', '.5')), fix_neg(int(odds[3:7]))]
        under = [float(odds[0:2].replace('½', '.5')), fix_neg(int(odds[-4:]))]
    elif len(odds) == 12:
        over = [float(odds[0]), fix_neg(int(odds[2:6]))]
        under = [float(odds[0]), fix_neg(int(odds[-4:]))]
    elif len(odds) == 16:
        # for lines with 1/2 and double digits
        over = [float(odds[0:3].replace('½', '.5')), fix_neg(int(odds[4:8]))]
        under = [float(odds[0:3].replace('½', '.5')), fix_neg(int(odds[-4:]))]
    else:
        # could add something for triple digit NCAAF lines
        if len(odds) > 0:
            print(odds)
        return None, None
    return over, under


def fix_neg(odds):
    """Sometimes even odds are displayed as -100"""
    if odds == -100:
        return 100
    else:
        return odds
