import itertools as it


def compare_ml(lines, sport):
    """Compares moneylines by comparing all away odds vs all home odds."""
    breaker = '\n' + '-' * 50 + '\n'
    value = []
    for game in lines:
        combos = it.product(game['away_odds'].items(), game['home_odds'].items())
        value.extend([f'{sport} {game["game"]} {combo[0]} {combo[1]} {breaker}' for combo in combos
                      if combo[0][1] + combo[1][1] >= 0])

    return value


def compare_spreads(lines, sport):
    """Compares spreads by comparing all away lines and odds vs all home lines and odds."""
    breaker = '\n' + '-' * 50 + '\n'
    value = []
    for game in lines:
        combos = it.product(game['away_odds'].items(), game['home_odds'].items())
        value.extend([f'{sport} {game["game"]} {combo[0]} {combo[1]} {breaker}' for combo in combos
                      if combo[0][1][0] + combo[1][1][0] >= 0 and combo[0][1][1] + combo[1][1][1] >= 0])

    return value


def compare_totals(lines, sport):
    """Compares totals by comparing all away lines and odds vs all home lines and odds."""
    breaker = '\n' + '-' * 50 + '\n'
    value = []
    for game in lines:
        combos = it.product(game['overs'].items(), game['unders'].items())
        value.extend([f'{sport} {game["game"]} {combo[0]} {combo[1]} {breaker}' for combo in combos
                      if combo[0][1][0] - combo[1][1][0] >= 0 and combo[0][1][1] + combo[1][1][1] >= 0])

    return value
