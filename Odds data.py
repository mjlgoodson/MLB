import csv
import datetime
import requests

# Function to fetch odds data from the Odds API
def fetch_odds(date, sport):
    api_key = '71b8c68e18eb6558aded4c8084d1ae92'
    endpoint = f'https://api.the-odds-api.com/v4/odds?apiKey={api_key}&sport={sport}&region=us&mkt=h2h&dateFormat=iso&oddsFormat=american&date={date}'
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to convert odds format
def convert_odds(odds):
    if odds.startswith('-'):
        return float(odds[1:]) / 100 + 1
    elif odds.startswith('+'):
        return 100 / (float(odds[1:]) / 100 + 1)
    else:
        return float(odds)

# Specify the start and end dates for the historical data
start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime.now()

# Create a CSV file and write header
with open('mlb_odds_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Date', 'Home Team', 'Away Team', 'Home Score', 'Away Score',
                  'Sportsbook', 'Spread', 'Spread Odds', 'Over/Under', 'Over/Under Odds']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate over each day and retrieve MLB games data
    current_date = start_date
    while current_date <= end_date:
        formatted_date = current_date.strftime('%Y-%m-%d')
        odds_data = fetch_odds(formatted_date, 'baseball_mlb')

        if odds_data:
            for game in odds_data['data']:
                home_team = game['home_team']
                away_team = game['teams'][0]
                home_score = None  # You may need to retrieve this from another source
                away_score = None  # You may need to retrieve this from another source
                sportsbook = game['site_key']
                spread = convert_odds(game['sites'][0]['odds']['spreads']['odds'])
                spread_odds = convert_odds(game['sites'][0]['odds']['spreads']['points'])
                over_under = convert_odds(game['sites'][0]['odds']['totals']['odds'])
                over_under_odds = convert_odds(game['sites'][0]['odds']['totals']['points'])

                # Write data to CSV file
                writer.writerow({'Date': formatted_date, 'Home Team': home_team, 'Away Team': away_team,
                                 'Home Score': home_score, 'Away Score': away_score, 'Sportsbook': sportsbook,
                                 'Spread': spread, 'Spread Odds': spread_odds, 'Over/Under': over_under,
                                 'Over/Under Odds': over_under_odds})

        current_date += datetime.timedelta(days=1)

print("Data saved to mlb_odds_results.csv")
