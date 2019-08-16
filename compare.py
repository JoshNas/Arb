
def compare_ml(lines, sport):
    """Compares moneylines by comparing all away odds vs all home odds."""
    breaker = '\n' + '-' * 50 + '\n'
    value = []
    for game in lines:
        for away_site in game['away_odds']:
            for home_site in game['home_odds']:
                away_ml = game['away_odds'].get(away_site)
                home_ml = game['home_odds'].get(home_site)
                print(f"Comparing {game['game']} {away_site} {away_ml} vs {home_site} {home_ml}\n")
                if away_ml + home_ml >= 0:
                    teams = game['game']
                    if sport == 'NFL' or sport == 'NCAAF':
                        split = teams.split('vs')
                        value.append(f'Value on {sport} {teams} at {away_site} {split[0].strip()} {away_ml} vs '
                                     f'{home_site} {split[1].strip()} {home_ml} {breaker}')
                    else:
                        # MLB
                        split = teams.split(' ')
                        value.append(f'Value on {sport} {teams} at {away_site} {split[0]} {away_ml} vs '
                                     f'{home_site} {split[2]} {home_ml} {breaker}')
    return value


def compare_spreads(lines, sport):
    """Compares spreads by comparing all away lines and odds vs all home lines and odds."""
    breaker = '\n' + '-' * 50 + '\n'
    value = []
    for game in lines:
        for away_site in game['away_odds']:
            for home_site in game['home_odds']:
                away_spread = game['away_odds'].get(away_site)[0]
                away_odds = game['away_odds'].get(away_site)[1]
                home_spread = game['home_odds'].get(home_site)[0]
                home_odds = game['home_odds'].get(home_site)[1]
                # print(f"Comparing {game['game']} {away_site} {away_spread} {away_odds} vs "
                #       f"{home_site} {home_spread} {home_odds}\n")
                if away_spread + home_spread >= 0 and away_odds + home_odds >= 0:
                    teams = game['game']
                    if sport == 'NFL' or sport == 'NCAAF':
                        split = teams.split('vs')
                        value.append(f'Value on {sport} {teams} at {away_site} {split[0].strip()} '
                                     f'{away_spread} {away_odds} vs {home_site} {split[1].strip()} '
                                     f'{home_spread} {home_odds} {breaker}')
                    else:
                        split = teams.split(' ')
                        value.append(f'Value on {sport} {teams} at {away_site} {split[0]} '
                                     f'{away_spread} {away_odds} vs {home_site} {split[2]} '
                                     f'{home_spread} {home_odds} {breaker}')
    return value


def compare_totals(lines, sport):
    """Compares totals by comparing all away lines and odds vs all home lines and odds."""
    breaker = '\n' + '-' * 50 + '\n'
    value = []
    for game in lines:
        for over_site in game['overs']:
            for under_site in game['unders']:
                over = game['overs'].get(over_site)[0]
                over_odds = game['overs'].get(over_site)[1]
                under = game['unders'].get(under_site)[0]
                under_odds = game['unders'].get(under_site)[1]
                # print(f"Comparing {game['game']} {over_site} {over} {over_odds} vs "
                #       f"{under_site} {under} {under_odds}\n")
                if over - under < 0 and over_odds + under_odds >= 0:
                    teams = game['game']
                    value.append(f'Value on {sport} {teams} at {over_site} over {over} {over_odds} vs '
                                 f'{under_site} under {under} {under_odds} {breaker}')
    return value
