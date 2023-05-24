import pandas as pd


def get_batter_stats(start_year = 1871, end_year = 2023, full_seasons_only=True):
    
    # read batting stats csv
    url = 'https://raw.githubusercontent.com/chadwickbureau/baseballdatabank/master/core/Batting.csv'
    batting_stats = pd.read_csv(url)
    
    # keep desired years
    batting_stats = batting_stats[(batting_stats['yearID'] >= start_year) & 
                                  (batting_stats['yearID'] <= end_year)]
    
    # remove non-full seasons if full_seasons_only == True
    non_full_seasons = [1995, 2020, 2023]
    if full_seasons_only:
        for season in non_full_seasons:
            batting_stats = batting_stats[batting_stats['yearID'] != season]
    
    return batting_stats 

def save_data(df, filename = 'batting'):
    df.to_csv(f'{filename}.csv', index=False)


# Work in Progress
# Tried to grab data from Baseball Reference

# from bs4 import BeautifulSoup
# import requests


# def get_mlb_acronyms():
    
#     url = 'https://www.baseball-reference.com'
#     source = requests.get(url).text # html of website
    
#     soup = BeautifulSoup(source, 'lxml')
    
#     # All team acronyms are in the first `div` tag with  
#     # class = "formfield". They are then in option tags (except the first).
#     div_formfield = soup.find_all('div', class_='formfield')[0]
#     option_tags = div_formfield.find_all('option')[1:]
    
#     # Should be 30 acronyms
#     team_acronyms = [str(tag)[15:18] for tag in option_tags]

    
#     return team_acronyms

# def get_batting_stats(start_year = 2010, end_year = 2023, full_seasons_only=True):
    
#     for year in range(start_year, end_year + 1):
        
#         # skip non-full seasons
#         if full_seasons_only:
#             if year == 2023 or year == 2020:
#                 continue
        
#         # read url with pandas
#         url = f'https://www.baseball-reference.com/leagues/majors/{year}.shtml#teams_standard_pitching'
#         temp_df = pd.read_html(url)[0].iloc[:30,:]
        
#         # create year column
#         temp_df['year'] = year
        
#         # if first year, start batting_df with temp_df, or else concat temp_df to batting_df
#         if year == start_year:
#             batting_df = temp_df
#         else:
#             batting_df = pd.concat([batting_df, temp_df])
      
#     return batting_df


# def get_pitching_stats(start_year = 2010, end_year = 2023, full_seasons_only=True):
    
#     for year in range(start_year, end_year + 1):
        
#         # skip non-full seasons
#         if full_seasons_only:
#             if year == 2023 or year == 2020:
#                 continue
        
#         # read url with pandas
#         url = f'https://www.baseball-reference.com/leagues/majors/{year}-standard-pitching.shtml'
#         temp_df = pd.read_html(url)[0].iloc[:30,:]
        
#         # create year column
#         temp_df['year'] = year
        
#         # if first year, start batting_df with temp_df, or else concat temp_df to batting_df
#         if year == start_year:
#             pitching_df = temp_df
#         else:
#             pitching_df = pd.concat([pitching_df, temp_df])
    
#     return pitching_df