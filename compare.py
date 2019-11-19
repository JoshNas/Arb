import itertools as it


def moneylines(lines, sport):
    """Compares moneylines by comparing all away odds vs all home odds."""
    value = []
    for game in lines:
        combos = it.product(game['away_odds'].items(), game['home_odds'].items())
        value.extend([f'{sport} {game["game"]} {combo[0][0]} {combo[0][1]} and {combo[1][0]} {combo[1][1]}\n\n'
                      for combo in combos if combo[0][1] + combo[1][1] >= 0])

    return value


def spreads(lines, sport):
    """Compares spreads by comparing all away lines and odds vs all home lines and odds."""
    value = []
    for game in lines:
        combos = it.product(game['away_odds'].items(), game['home_odds'].items())
        try:
            value.extend([f'{sport} {game["game"]} {combo[0][0]}: {combo[0][1][0]} {combo[0][1][1]} and '
                          f'{combo[1][0]}: {combo[1][1][0]} {combo[1][1][1]}\n\n' for combo in combos
                          if combo[0][1][0] + combo[1][1][0] >= 0 and combo[0][1][1] + combo[1][1][1] >= 0])
        except TypeError:
            print(combos)

    return value


def totals(lines, sport):
    """Compares totals by comparing all away lines and odds vs all home lines and odds."""
    value = []
    for game in lines:
        combos = it.product(game['unders'].items(), game['overs'].items())
        value.extend([f'{sport} {game["game"]} {combo[0][0]}: {combo[0][1][0]} {combo[0][1][1]} and '
                      f'{combo[1][0]}: {combo[1][1][0]} {combo[1][1][1]}\n\n' for combo in combos
                      if combo[0][1][0] - combo[1][1][0] >= 0 and combo[0][1][1] + combo[1][1][1] >= 0])

    return value
