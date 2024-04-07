import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
team_batting_stats = pd.read_csv("team_batting_stats_2024_with_advanced_metrics.csv")
team_pitching_stats = pd.read_csv("team_pitching_stats_2024_with_advanced_metrics.csv")

# Basic exploration
print("Team Batting Stats Overview:\n", team_batting_stats.describe())
print("\nTeam Pitching Stats Overview:\n", team_pitching_stats.describe())

# Checking for missing values
print("\nMissing values in Team Batting Stats:\n", team_batting_stats.isnull().sum())
print("\nMissing values in Team Pitching Stats:\n", team_pitching_stats.isnull().sum())

# Visualize the distribution of team batting averages (BA)
plt.figure(figsize=(8, 6))
sns.histplot(team_batting_stats['BA'], kde=True, bins=20)
plt.title('Distribution of Team Batting Averages')
plt.xlabel('Batting Average')
plt.ylabel('Frequency')
plt.show()

# Correlation heatmap for team batting stats
plt.figure(figsize=(10, 8))
sns.heatmap(team_batting_stats.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix for Team Batting Stats')
plt.show()

# Correlation heatmap for team pitching stats
plt.figure(figsize=(10, 8))
sns.heatmap(team_pitching_stats.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix for Team Pitching Stats')
plt.show()

# Scatter plot of ERA vs. WHIP for teams
plt.figure(figsize=(8, 6))
sns.scatterplot(x='ERA', y='WHIP', data=team_pitching_stats)
plt.title('Relationship between ERA and WHIP')
plt.xlabel('ERA')
plt.ylabel('WHIP')
plt.show()

# Scatter plot of Team OPS vs. Wins (Modify as needed based on available data)
# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='OPS', y='Wins', data=team_batting_stats)
# plt.title('Team OPS vs. Wins')
# plt.xlabel('OPS')
# plt.ylabel('Wins')
# plt.show()

# Note: The last plot requires you to have or join data on team wins. You might need to adjust it based on your dataset.
