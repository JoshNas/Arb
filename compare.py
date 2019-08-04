

def compare_ml(lines):
    """Compares moneylines by comparing all away odds vs all home odds."""
    breaker = '\n' + '-' * 50 + '\n'
    value = []
    # Wasting some time by comparing sites to themselves. Is there a way to fix this that actually saves time?
    for game in lines:
        # compare one sites away odds vs all home odds
        for away_site in game['away_odds']:
            try:
                away_ml = game['away_odds'].get(away_site)
            except TypeError:
                break

            for home_site in game['home_odds']:
                try:
                    home_ml = game['home_odds'].get(home_site)
                except TypeError:
                    break
                # if away_ml and home_ml:
                #     teams = game['game']
                #     split = teams.split(' ')
                #     print(f'Comparing {teams} at {away_site} {split[0]} {away_ml} vs '
                #           f'{home_site} {split[2]} {home_ml} {breaker}')
                if away_ml + home_ml >= 0:
                    teams = game['game']
                    split = teams.split(' ')
                    # print(f'Value on {teams} at {away_site} {away_ml} vs {home_site} {home_ml} {breaker}')
                    value.append(f'Value on {teams} at {away_site} {split[0]} {away_ml} vs '
                                 f'{home_site} {split[2]} {home_ml} {breaker}')

    return value


def compare_spreads(lines):
    """Compares spreads by comparing all away lines and odds vs all home lines and odds."""
    breaker = '\n' + '-' * 50 + '\n'
    value = []
    # Wasting some time by comparing sites to themselves. Is there a way to fix this that actually saves time?
    for game in lines:
        for away_site in game['away_odds']:
            # compare one sites away odds vs all home odds
            try:
                away_spread = game['away_odds'].get(away_site)[0]
                away_odds = game['away_odds'].get(away_site)[1]
            except TypeError:
                break
            for home_site in game['home_odds']:
                try:
                    home_spread = game['home_odds'].get(home_site)[0]
                    home_odds = game['home_odds'].get(home_site)[1]
                except TypeError:
                    break

                teams = game['game']
                split = teams.split(' ')

                print(f'Comparing {teams} at {away_site} {split[0]} {away_spread} {away_odds} vs '
                      f'{home_site} {split[2]} {home_spread} {home_odds} {breaker}')
                if away_spread + home_spread >= 0 and away_odds + home_odds >= 0:
                    teams = game['game']
                    split = teams.split(' ')
                    value.append(f'Value on {teams} at {away_site} {split[0]} {away_spread} {away_odds} vs '
                                 f'{home_site} {split[2]} {home_spread} {home_odds} {breaker}')

    return value


def compare_totals(lines):
    """Compares totals by comparing all away lines and odds vs all home lines and odds."""
    breaker = '\n' + '-' * 50 + '\n'
    value = []
    # Wasting some time by comparing sites to themselves. Is there a way to fix this that actually saves time?
    for game in lines:
        for over_site in game['over_odds']:
            # compare one sites away odds vs all home odds
            try:
                try:
                    over = game['over_odds'].get(over_site)[0]
                except IndexError:
                    break
                over_odds = game['over_odds'].get(over_site)[1]
            except TypeError or IndexError:
                print(game)
                break
            for under_site in game['under_odds']:
                try:
                    under = game['under_odds'].get(under_site)[0]
                    under_odds = game['under_odds'].get(under_site)[1]
                except TypeError:
                    break
                # teams = game['game']
                # print(f'Comparing {teams} at {over_site} {over } {over_odds} vs '
                #       f'{under_site} {under} {under_odds} {breaker}')
                if over + under >= 0 and over_odds + under_odds >= 0:
                    teams = game['game']

                    value.append(f'Value on {teams} at {over_site} {over} {over_odds} vs '
                                 f'{under_site} {under} {under_odds} {breaker}')

    return value
