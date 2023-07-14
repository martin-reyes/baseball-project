<a name="top"></a>

# Baseball Analysis

This repo is made to provide baseball data to perform analysis, (statistical) tests/simulations, and (ML) modeling. Feel free to create a new notebook or python file if you have any analyses or models you want to run.

Possible project goals:

- Which stats lead to more wins (team wins)? (EDA)
    - Can we build a regression model to predict team wins in a season?
- Which stats correlate most to runs scored (team runs)? (EDA)
    - Can we build a regression model to predict team runs in a season?
- Which stats correlate most to other important stats, including player stats? (EDA)
    - Can we build a regression model to predict these stats?

Projects:
- **[Project 1](#project1): Predicting Team Wins + EDA**
    
## Acquire Data

[See Data Dictionary](#date-dictionary)

- Using Selenium to read mlb team and player stats from [Baseball Reference](https://www.baseball-reference.com)

Note on the data: 
- There are only 30 teams, so although there are lots of features (stats), there can only be so many rows of data, as each row represents the team's stats for the year. The amount of rows is 30 times the number of years.
- Players' stats, on the other hand, can offer thousands of rows to analyze.
- 2020 and 2023 data don't offer a full season's worth of stats, so these are left out, but can be accessed with the functions in `acquire.py`

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
        - also think about how to join the tables. We can't merely join on player name, as players share names. And we can't only join on player ID because these are duplicated. maybe join on a combination of columns.
    - don't combine pitcher and batter data


---
<a name="project1"></a>

## Project 1: Predicting MLB Team Wins + Analyzing Stats to Team Wins

**Description:**
- In this project, we will use **team pitching stats** and **team batting stats** to see which stats lead to more wins. After finding the most predictive features, we will run regression models to predict team wins in a season.

**Goals:**

- EDA: 
    - gain insights on stats the are important for wins
    - visualize insights
- Modeling:
    - Create regression models
        - For best regression model, interpret results (e.g. coefficients) for insights



- Features: MLB stats, except team wins
- Target: team wins (continuous)


### Explore and Analysis

- Tasks:
    - Explore correlations for team wins along with each numerical stat
        - Explore correlations
        - Visualize with scatterplots, heatmaps, histograms, etc.
            - e.g. scatterplot with wins on y axis and runs scored on x-axis
        - **most of our features are continuous**
    - Explore relationships for team wins along with each categorical stat
        - Explore numerical stats for wins by category
            - e.g. see average wins by team.
        - Visualize with bar charts of average wins
        - Visualize win distributions for each category.
            - e.g. boxplots, histograms, and/or stripplots by team

### Modeling



### Conclusions and Insights












[Back to top](#top)

---

<a name="data-dictionary"></a>

## Data Dictionary

**Team Batting Stats:**

| Stat    | Definition                                 | Stat    | Definition                      |
|:--------|:-------------------------------------------|:--------|:------------------------------------|
| year    | Season                                     | #Bat    | Number of batters           |
| W       | Wins                                       | L       | Losses                       |
| W-L%    | Win-loss percentage                        | Tm      | Team name                      |
| G       | Games played                               | PA      | Plate appearances             |
| AB      | At-bats                                    | R       | Runs scored                      |
| H       | Hits                                       | 2B      | Doubles                           |
| 3B      | Triples                                    | HR      | Home runs                     |
| RBI     | Runs batted in                             | SB      | Stolen bases                   |
| CS      | Caught stealing                            | BB      | Walks                             |
| SO      | Strikeouts                                 | BA      | Batting average                  |
| OBP     | On-base percentage $\frac{H + BB + HBP}{AB + BB + HBP + SF}$  | SLG     | Slugging percentage $\frac{TB}{AB}$  |
| OPS     | On-base plus slugging                       | OPS+    | Adjusted OPS                  |
| TB      | Total bases                                | GDP     | Grounded into double play           |
| HBP     | Hit by pitch                               | SH      | Sacrifice hits                  |
| SF      | Sacrifice flies                            | IBB     | Intentional walks                 |
| LOB     | Left on base                               | rOBA    | Reference-weighted on-base average, a measure of a player's offensive contributions  |
| BAbip   | Batting average on balls in play $\frac{H - HR}{AB - SO - HR + SF}$ | Rbat+   | Adjusted runs above average, batting runs as computed for WAR  |
| ISO     | Isolated power $\frac{TB - H}{AB}$          | HR%     | Home run percentage $\frac{HR}{PA}$   |
| SO%     | Strikeout percentage     $\frac{SO}{PA}$    | BB%     | Walk percentage  $\frac{BB}{PA}$     |
| EV      | Exit velocity                              | HardH%  | Percentage of hard-hit balls     |
| LD%     | Line drive percentage                      | GB%     | Ground ball percentage       |
| FB%     | Fly ball percentage                        | GB/FB   | Ground ball to fly ball ratio     |
| Pull%   | Percentage of pulled balls                  | Cent%   | Percentage of balls hit to center field|
| Oppo%   | Percentage of balls hit to opposite field   | WPA     | Win probability added    |
| cWPA    | Championship win probability added      | RE24    | Run expectancy based on 24 base-out states|
| RS%     | Percentage of runs scored                   | SB%     | Stolen base success rate       |
| XBT%    | Extra bases taken percentage     | Outs    | Total outs made $(AB - H) + GIDP + SF + SH + CS$   |
| RC      | Runs created                               | RC/G    | Runs created per game        |
| AIR     | Measure of amount played in hitter-friendly setting  | lgBA    | Adjusted batting average |
| lgOBP   | Adjusted on-base percentage                  | lgSLG   | Adjusted slugging percentage  |
| lgOPS   | Adjusted on-base plus slugging                | OWn%    | Offensive winning percentage, percentage of games a team with nine of this player batting would win |
| BtRuns  | Adjusted Batting Runs                 | BtWins  | Adjusted Batting Wins |
| TotA | Total chances in the field $\frac{TB + HBP + BB + SB - CS}{AB - H + CS + GIDP}$ | SecA | Secondary average $\frac{TB - H + BB + SB - CS}{AB}$ |
| PwrSpd  | Power-speed number  $\frac{2 x HR x SB}{SB + HR}$               |


**Player Batting Stats:**

| Stat         | Definition                                            | Stat         | Definition        |
|:-------------|:------------------------------------------------------|:-------------|:------------------|
| year         | Season                                                | id           | Player ID         |
| Name         | Player Name                                     | Bats         | Bats right/left/switch |
| Age          | Player Age                                            | Tm           | Team             |
| Lg           | League                                                | G            | Games played     |
| PA           | Plate appearances                                     | AB           | At-bats           |
| R            | Runs scored                                           | H            | Hits             |
| 2B           | Doubles                                               | 3B           | Triples          |
| HR           | Home runs                                             | RBI          | Runs batted in    |
| SB           | Stolen bases                                          | CS           | Caught stealing   |
| BB           | Walks                                                 | SO           | Strikeouts       |
| BA           | Batting average                                       | OBP          | On-base percentage  |
| SLG          | Slugging percentage                                | OPS          | On-base plus slugging |
| OPS+         | OPS+                                                  | TB           | Total bases       |
| GDP          | Grounded into double play                              | HBP          | Hit by pitch   |
| SH           | Sacrifice hits                                        | SF           | Sacrifice flies   |
| IBB          | Intentional walks                                     | Pos Summary  | Positions played  |
| Outs         | Total outs made                                       | RC           | Runs created    |
| RC/G         | Runs created per game | AIR          | Measure of amount played in hitter-friendly setting|
| BAbip | Batting average on balls in play $\frac{H - HR}{AB - SO - HR + SF}$  | lgBA | Adjusted batting average |
| lgOBP        | League on-base percentage           | lgSLG        | League slugging percentage |
| lgOPS        | League on-base plus slugging    | OWn%         | Offensive winning percentage   |
| BtRuns       | Batting runs above average        | BtWins       | Batting wins above replacement    |
| TotA         | Total chances in the field                | SecA         | Secondary average          |
| ISO          | Isolated power                                        | PwrSpd       | Power-speed number |
| rOBA         | Reference-weighted on-base average                    | Rbat+        | Runs above average  |
| HR%          | Home run percentage                                 | SO%          | Strikeout percentage |
| BB%          | Walk percentage                                     | LD%          | Line drive percentage |
| GB%          | Ground ball percentage                                | FB%          | Fly ball percentage |
| GB/FB        | Ground ball to fly ball ratio         | Pull%        | Percentage of pulled balls  |
| Cent% | Percentage of balls hit to center field | Oppo%    | Percentage of balls hit to opposite field  |
| WPA          | Win probability added                 | cWPA         | Championship win probability added |
| RE24 | Run expectancy based on 24 base-out states           | RS%          | Percentage of runs scored |
| SB%          | Stolen base success rate                    | XBT%         | Extra bases taken percentage  |
| EV           | Exit velocity                               | HardH%       | Percentage of hard-hit balls |


**Team Pitching Stats:**

| Stat   | Definition                                         | Stat   | Definition               |
|:-------|:---------------------------------------------------|:-------|:-------------------------|
| year   | Year of the season                                 | Tm     | Team name        |
| #P     | Number of pitchers                                 | PAge   | Average age of pitchers   |
| RA/G   | Runs against per game                              | W      | Wins          |
| L      | Losses                                             | W-L%   | Win-loss percentage       |
| ERA    | Earned run average                                 | G      | Games played         |
| GS     | Games started                                      | GF     | Games finished      |
| CG     | Complete games                                     | tSho   | Team shutouts     |
| cSho   | Complete game shutouts                             | SV     | Saves          |
| IP     | Innings pitched                                    | H      | Hits allowed       |
| R      | Runs allowed                                       | ER     | Earned runs        |
| HR     | Home runs allowed                                  | BB     | Walks allowed        |
| IBB    | Intentional walks                                  | SO     | Strikeouts         |
| HBP    | Hit by pitch                                       | BK     | Balks           |
| WP     | Wild pitches                                       | BF     | Batters faced        |
| ERA+   | Adjusted ERA                                       | FIP    | Fielding Independent Pitching   |
| WHIP   | Walks plus hits per inning pitched                 | H9     | Hits per 9 innings      |
| HR9    | Home runs per 9 innings                            | BB9    | Walks per 9 innings    |
| SO9    | Strikeouts per 9 innings                           | SO/W   | Strikeout-to-walk ratio    |
| LOB    | Left on base                                      | BA     | Batting average against    |
| OBP    | On-base percentage against                        | SLG    | Slugging percentage against     |
| OPS    | On-base plus slugging against              | BAbip  | Batting average on balls in play against  |
| HR%    | Home run percentage against                       | SO%    | Strikeout percentage against  |
| BB%    | Walk percentage against                           | EV     | Exit velocity against           |
| HardH% | Percentage of hard-hit balls against               | LD%    | Line drive percentage against   |
| GB%    | Ground ball percentage against                    | FB%    | Fly ball percentage against     |
| GB/FB  | Ground ball to fly ball ratio against              | WPA    | Win probability added          |
| cWPA   | Championship win probability added        | RE24   | Run expectancy based on 24 base-out states |
| PAu    | Total plate appearances used by pitchers           | PA     | Plate appearances by pitchers     |
| AB     | At-bats by pitchers                                | 2B     | Doubles allowed               |
| 3B     | Triples allowed                                    | SB     | Stolen bases allowed          |
| CS     | Caught stealing allowed                            | TB     | Total bases allowed           |
| GDP    | Grounded into double play by pitchers              | SH     | Sacrifice hits by pitchers      |
| SF     | Sacrifice flies by pitchers                        | ROE    | Reached on error by pitchers    |
| Ptn%   | Pickoff percentage by pitchers           | SO-BB% | Strikeout-to-walk percentage by pitchers  |
| XBH%   | Extra-base hits percentage by pitchers | X/H%   | Extra-base hits to hits percentage by pitchers |
| GO/AO | Ground ball to fly ball ratio by pitchers | IP% | Percentage of team's innings pitched by pitchers|
| HR/FB  | Home run to fly ball ratio by pitchers  | IF/FB  | Infield fly ball to fly ball ratio by pitchers|
| Opp    | GIDP opportunities        | DP     | Double plays induced |
| %      | GIDP Percentage                                         |        |                               |

**Player Pitching Stats:**

| Stat   | Definition                                          | Stat   | Definition            |
|:-------|:----------------------------------------------------|:-------|:----------------------|
| year   | Year of the season                                  | id     | Player ID                     |
| Name   | Player Name                                         | Throws | Throwing hand                |
| Age    | Player Age                                          | Tm     | Team                        |
| Lg     | League                                              | W      | Wins                       |
| L      | Losses                                              | W-L%   | Win-loss percentage          |
| ERA    | Earned run average                                  | G      | Games played                    |
| GS     | Games started                                       | GF     | Games finished               |
| CG     | Complete games                                      | SHO    | Shutouts                    |
| SV     | Saves                                               | IP     | Innings pitched             |
| H      | Hits allowed                                        | R      | Runs allowed                 |
| ER     | Earned runs                                         | HR     | Home runs allowed           |
| BB     | Walks allowed                                       | IBB    | Intentional walks            |
| SO     | Strikeouts                                          | HBP    | Hit by pitch                   |
| BK     | Balks                                               | WP     | Wild pitches                  |
| BF     | Batters faced                                       | ERA+   | Adjusted ERA                 |
| FIP    | Fielding Independent Pitching                     | WHIP   | Walks plus hits per inning pitched |
| H9     | Hits per 9 innings                                  | HR9    | Home runs per 9 innings      |
| BB9    | Walks per 9 innings                                 | SO9    | Strikeouts per 9 innings       |
| SO/W   | Strikeout-to-walk ratio                             | BA     | Batting average against         |
| OBP    | On-base percentage against                         | SLG    | Slugging percentage against    |
| OPS    | On-base plus slugging against           | BAbip  | Batting average on balls in play against |
| HR%    | Home run percentage against                        | SO%    | Strikeout percentage against    |
| BB%    | Walk percentage against                            | LD%    | Line drive percentage against   |
| GB%    | Ground ball percentage against                     | FB%    | Fly ball percentage against   |
| GB/FB  | Ground ball to fly ball ratio against               | WPA    | Win probability added         |
| cWPA   | Championship win probability added      | RE24   | Run expectancy based on 24 base-out states  |
| EV     | Exit velocity against                            | HardH% | Percentage of hard-hit balls against |


[Back to top](#top)