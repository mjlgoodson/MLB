import pandas as pd
from pybaseball import team_batting, team_pitching
from datetime import datetime

# Fetch team-level batting and pitching statistics
def fetch_current_season_data(year):
    team_batting_stats = team_batting(year)
    team_pitching_stats = team_pitching(year)
    
    # Team Batting Average (BA)
    team_batting_stats['BA'] = team_batting_stats['H'] / team_batting_stats['AB']

    # Team On-base Plus Slugging (OPS)
    team_batting_stats['OPS'] = team_batting_stats['OBP'] + team_batting_stats['SLG']

    # Team WHIP (Walks + Hits per Innings Pitched)
    team_pitching_stats['WHIP'] = (team_pitching_stats['BB'] + team_pitching_stats['H']) / team_pitching_stats['IP']

    # Calculating wOBA for teams (using a simplified approach based on available stats)
    # Note: This is a very simplified calculation and will need to be updated and made more accurate
    wOBA_weights = {'uBB': 0.69, 'HBP': 0.72, '1B': 0.89, '2B': 1.27, '3B': 1.62, 'HR': 2.10}
    team_batting_stats['wOBA'] = (
        wOBA_weights['uBB'] * team_batting_stats['BB'] + 
        wOBA_weights['HBP'] * team_batting_stats['HBP'] + 
        wOBA_weights['1B'] * (team_batting_stats['H'] - team_batting_stats['2B'] - team_batting_stats['3B'] - team_batting_stats['HR']) +
        wOBA_weights['2B'] * team_batting_stats['2B'] +
        wOBA_weights['3B'] * team_batting_stats['3B'] +
        wOBA_weights['HR'] * team_batting_stats['HR']
    ) / (team_batting_stats['AB'] + team_batting_stats['BB'] - team_batting_stats['IBB'] + team_batting_stats['SF'] + team_batting_stats['HBP'])

    # FIP (Fielding Independent Pitching)
    FIP_constant = 3.10  # Constant set for 2024 
    team_pitching_stats['FIP'] = ((13*team_pitching_stats['HR'] + 3*(team_pitching_stats['BB'] + team_pitching_stats['HBP']) - 2*team_pitching_stats['SO']) / team_pitching_stats['IP']) + FIP_constant

    
    # Save to CSV
    team_batting_stats.to_csv(f"team_batting_stats_{year}_with_advanced_metrics.csv", index=False)
    team_pitching_stats.to_csv(f"team_pitching_stats_{year}_with_advanced_metrics.csv", index=False)

    print(f"Advanced data for the {year} season, calculated dynamically, saved to CSV files.")

if __name__ == "__main__":
    current_year = datetime.now().year
    fetch_current_season_data(current_year)
