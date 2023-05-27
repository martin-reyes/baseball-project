# Baseball Analysis

This repo is made to provide baseball data to perform analysis, (statistical) tests/simulations, and (ML) modeling. Feel free to create a new notebook or python file if you have any analyses or models you want to run.

Note on the data: 
- There are only 30 teams, so although there are lots of features (stats), there can only be so many rows of data, as each row represents the team's stats for the year. The amount of rows is 30 times the number of years.
- Players' stats, on the other hand, can offer thousands of rows to analyze.
- 2020 and 2023 data don't offer a full season's worth of stats, so these are left out, but can be accessed with the functions in `acquire.py`

Possible questions to answer and tasks to do:

#### Join team DataFrames

- Desired Result(s):
    - team_batting.csv: combine batting stats for all years (2005 - 2022)
    - team_pitching.csv: combine pitching stats for all years
    - **maybe** team_stats.csv: combine batting and pitching stats for all years
        - might be better to keep pitching and batting stats separate
- assuming these csv's are joined right, we can save them and delete the original csv's. 

#### Join player DataFrames

- Desired Result(s): 
    - combine 2005-2014 data with 2015-2022 data
    - combine metrics (standard, advanced, sabermetric).
        - this may be a tougher task because the rows for each metric don't match (i.e. `player_batting_advanced.csv` doesn't have the same number of rows as `player_batting_standard.csv`)
        - also think about how to join the tables. You can't merely join on player name, as players share names. And you can't only join on player ID because these are duplicated. maybe join on a combination of columns.
    - don't combine pitcher and batter data



#### Explore and Analysis

Ideas for EDA:

- explore which stats most relate to wins and/or runs scored
- explore which stats relate to others


Visualization ideas:


#### Stats Testing

Ideas for Testing:


#### Modeling

Ideas for models:
