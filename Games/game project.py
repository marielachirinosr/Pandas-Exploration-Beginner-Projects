import pandas as pd

# Read the game data
game_cv = pd.read_csv('Games/vgsales.csv')

# N Games by Platform and Year
game_by_platform = game_cv.groupby(['Platform', 'Year']).size().reset_index(name='Counts')
game_cv = game_cv.merge(game_by_platform, on=['Platform', 'Year'])
print("Games by Platform and Year:\n", game_cv)

# N Games by Genre
game_by_genre = game_cv.groupby(['Genre', 'Publisher']).size().reset_index(name='Counts')
game_cv = game_cv.merge(game_by_genre, on=['Genre', 'Publisher'])
print("Games by Genre:\n", game_cv)

# Top 10 sales in North America (NA)
top_10_na_sales = game_cv.nlargest(10, 'NA_Sales')
columns_to_display_na = ['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales']
result_df_na = top_10_na_sales[columns_to_display_na]
print("Top 10 Sales in North America:\n", result_df_na)

# Top 10 lowest sales in Europe (EU)
game_cv_eu_sales = game_cv[game_cv['EU_Sales'] >= 1.00]
top_10_lowest_eu_sales = game_cv_eu_sales.nsmallest(100, 'EU_Sales')
columns_to_display_eu = ['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'EU_Sales']
result_df_eu = top_10_lowest_eu_sales[columns_to_display_eu]
print("Top 10 Lowest Sales in Europe:\n", result_df_eu)

# JP_Sales equal to 2.0 or >= 2.0
filtered_game_cv_jp_sales = game_cv[game_cv['JP_Sales'] >= 2.0][
    ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'JP_Sales']
]
print("Games with JP_Sales >= 2.0:\n", filtered_game_cv_jp_sales)

# Value counts by Publisher and Year
game_counts = game_cv.groupby(['Publisher', 'Year']).size().reset_index(name='Counts')
print("Game Counts by Publisher and Year:\n", game_counts)

# Order by publisher and year, mean global sales
game_by_global = game_cv.groupby(['Publisher', 'Year']).agg(
    {'Rank': 'mean', 'Name': 'first', 'Platform': 'first', 'Genre': 'first', 'Global_Sales': 'mean'}
).reset_index()
print("Mean Global Sales by Publisher and Year:\n", game_by_global)
