# 2025 LFFL Draft Research

## GenAI Instructions
When doing any sort of analysis, always follow these general rules:
1. Any analysis should be done from a dynasty perspective:  Not a redraft league perspective.  Rookies have a much higher priority in the rookie draft.
2. `2025-my-active-roster.csv` should be used to learn about my current team roster.
3. `2025-fantasy-pros-rookie-rankings--2025-06-24.csv` should always be used to determine the most probable draft position for each player in the LFFL draft.  For example, Ashton Jeanty and Omarion Hamption are listed as the top two picks.  It is not likely they will still be present when it is my turn to pick.
4. Also look at `2025-available-2025-05-23-all.csv` to determine at one place in the rookie draft a player might get selected.  Also take into account `2025-06-27--updated-rookie-rankings--advice.csv`
5. Use `2025-mel-kiper-1st-round.csv`, `2025-nfl-dot-com-1st-round.csv`, `2025-pff-1st-round.csv`, `2025-fantasy-pros-1st-round-with-trades.csv`, and `2025-pff-7-rounds.csv` to determine how actual draft position might rise or fall from the order provided in `2025-fantasy-pros-rookie-rankings.csv` by aggregating the data and taking into consideration the delta between the aggregated data and the suggest ranking in `2025-fantasy-pros-rookie-rankings.csv`.
6. Use the notes column from `2025-06-27--updated-rookie-rankings--advice.csv`, `2025-nfl-dot-com-1st-round.csv`, `2025-pff-1st-round.csv`, `025-fantasy-pros-1st-round-with-trades.csv`, and `2025-pff-7-rounds.csv` to understand the reasoning behind the pick.  This information should be strongly considered when identifying the potential fantasy impact a player might have.
7. Use `2025-pff-7-rounds.csv` when looking for picks beyond the first round.
8. Use `2025-available-2025-05-23-all.csv` to see how any rookie suggestion compares to the available veterans
9. Reference the `Glossary` section below to identify unknown terms
10. Use the `Positions` section below to understand the role each position plays in fantasy football
11. Refer to the `League Format` section to better understand the league rules that will impact draft value of each player.
12. Use the `LFFL Draft Format` section to understand how the draft works and what picks I have for the 2025 draft.
13. Use the `My Draft Preferences` section to understand how I evaluate picks and take this heavily into considerations when deciding who I should take

## Glossary
* Sleeper - A "sleeper" is a player that is picked later in the draft that is likely to outperform players picked before them.
* Dynasty League - Unlike traditional redraft fantasy football leagues, dynasty leagues draft rookies and keep the same team year after year.
* PPR - Point per reception, this means that players get an additional fantasy point for each catch.
* Flex - This means the position on the roster can be occupied by a WR, RB, or TE.
* K - This means "kicker".  This position should be ignored for any analysis.
* DST - This means "defense and special teams".  This position should be ignored for any analysis.
* Taxi Squad - A portion of the team that can hold rookies for up to three years.  These players cannot be used as starters.
* ECR - Expert consensus ranking (an average of all rankings by fantasy football experts)
* ADP - Average draft position (the average of the position the player is being drafted across all league drafts)
* ECR vs. ADP - A metric that shows how the average manager sentiment towards a given player differs from that of experts.  A negative number indicates that managers don't value a player as highly as the experts while a positive number indicates that managers see more value in a given player than the experts do.  This can be helpful will determining where players might actually end up going in a draft and for identifying potential sleepers.

## Positions
Fantasy football does not value players the same way the real NFL does.  Fantasy football only cares about the following positions:  All other can be ignored:
* Quarterback (QB or Q) - An important position in all fantasy formats.
* Wide Receiver (WR) - This position has higher importance in PPR leages as it gets 1 point per reception
* Running Back (RB or HB) - For PPR, running backs are not valued as highly as top wide receivers; however, if the running back is known to be able to catch passes out of the backfield, this increases their value.
* Tight Ends (TE) - Not valued as highly as WR or RB; however, the gap between the top tier TEs and second TEs is pretty big.  This means getting a TE is worthwhile only if they are one of the best.

## League Format
* The LFFL dynasty fantasy league is a PPR league with 6 managers.
* Each team starts two QBs, 3 WRs, 3 RBs, 2 TE, 3 Flex, 1 K, and 1 DST each week.
* Each team can have up to five rookies on their taxi squad.

## LFFL Rookie Draft Format
* The LFFL rookie draft is 4 rounds long:  Each round has 6 picks.
* Each manager starts with one pick per round; however, this can change as a result of trades.
* I have the 5th (1.5), 7th (2.1), 17th (3.5), and 20th (4.2) picks in the 2025 LFFL Rookie Draft.
* The other managers in the league have a tendancy to draft players from Ohio State.

## LFFL Veteran Draft Format
* The LFFL rookie draft is 2 rounds long:  Each round has 6 picks.
* Each manager starts with one pick per round; however, this can change as a result of trades.
* I have the 1st (1.1) and 11th (2.5) picks in the 2025 LFFL Veteran Draft.
* The other managers in the league have a tendancy to draft players from Ohio State.

## My Draft Preferences
* I always look at the data in `2025-my-active-roster.csv` to identify areas of need.  To do this, I:
  * Look at the player rankings for each position.
  * I first identify positions where I don't have enough highly ranked players for my starting roster.
  * Then I look for areas where I have large gaps in ranking.  For example, at WR I have a large gap between Cooper Kupp and Josh Downs.  At TE, I have a large gap between Mark Andrews and Pat Freiermuth.
* Once I know my areas of need, I look at the best players at those positions that might be available when I make my picks.
* If there is a very good or sleeper RB available in the rookie draft, I may ignore my area of need and take that player.
* With my last rookie pick I like to look for a sleeper pick.
* This year I am leaning towards taking a good veteran WR with my first pick in the veteran draft.  When determining rookie draft pick recommendations, this should be taken into account.

## Description of files in the repository
`2025-available-2025-05-23-all.csv`
* This file contains a list of the top 160 players available for draft in both the rookie and veteran drafts
* The player rankings are based on ADP as of 05/23/2025
* This file provides insight into how rookies are ranked against the available veterans
* This file also shows how veterans compare to the available rookies

`2025-my-active-roster.csv`
* This file contains a breakdown of my team.  The players are ranked by dynasty value.
* This file should be used as a basis when making decisions about who I should draft.
* Column Details
  * 1 - Rank on my team (If this column does not have a number, that means the player is not on my team, but I have interest in them)
  * 2 - Player name
  * 3 - Dynasty Nerds ranking for the player for their specific position
  * 4 - Ignore this column
  * 5 - ESPN ranking for the player for their specific position
  * 6 - ESPN overall ranking for the player
  * 7 - PFF ranking for the player for their specific position
  * 8 - PFF overall ranking for the player
  * 9 - Ignore this column
  * 10 - FantasyPros ranking for the player for their specific position
  * 11 - FantasyPros overall ranking for the player
  * 12 - FantasyPros tier for that player for their specific position
* * All data in a given row relates to the player identified in column `2`.

`2025-fantasy-pros-rookie-rankings--2025-04-24.csv`
* This file contains an ordered ranking of the rookies available in the 2025 NFL draft from a dynasty fantasy football perspective.
* Column Details
  * 1 - Overall dynasty fantasy football rank for 2025 drafts
  * 2 - Player name
  * 3 - Position the player plays
  * 4 - Highest possible draft position
  * 5 - Lowest possible draft position
  * 6 - Average draft position
  * 7 - Standard deviation
* All data in a given row relates to the player identified in column `2`.

`2025-fantasy-pros-rookie-rankings--2025-06-20.csv`
* This is an updated version of the above file.  It contains the same data, but with updated rakings.
* Column Details
  * 1 - Overall dynasty fantasy football rank for 2025 drafts
  * 2 - Player name
  * 3 - Position the player plays
  * 4 - Highest possible draft position
  * 5 - Lowest possible draft position
  * 6 - Average draft position
  * 7 - Standard deviation
  * 8 - ECR vs ADP
* All data in a given row relates to the player identified in column `2`.

`2025-06-27--updated-rookie-rankings--advice.csv`
* This is an updated version of the above file.  It contains the same data, but with updated rakings and some very important notes for most players from a dynasty perspective.  Strongly consider the data in this file when analyzing players to pick.
* Column Details
  * 1 - Overall dynasty fantasy football rank for 2025 drafts
  * 2 - Player name
  * 3 - Position the player plays
  * 4 - Age of player (generally, younger is better)
  * 5 - Highest possible draft position
  * 6 - Lowest possible draft position
  * 7 - Average draft position
  * 8 - Standard deviation
  * 9 - ECR vs ADP
  * 10 - Tier
  * 11 - Notes
* All data in a given row relates to the player identified in column `2`.

`2025-mel-kiper -1st-round.csv`
* This file contains Mel Kiper's analysis of the first rounds picks in the NFL draft.
* Column Details
  * 1 - Overall expected pick (across all rounds of the draft)
  * 2 - Expected pick within a single round
  * 3 - The team that is expected to draft the player
  * 4 - The player's name
  * 5 - The player's position
  * 6 - The college the player attended
  * 7 - Ignore this column
  * 8 - Ignore this column
* All data in a given row relates to the player identified in column `2`.

`2025-fantasy-pros-1st-round-with-trades.csv`
* This file contains Fantasy Pro's analysis of the first rounds picks in the NFL draft.
* Unlike the other files, this one takes into consideration potential trades that NFL team might make.
* Column Details
  * 1 - Overall expected pick (across all rounds of the draft)
  * 2 - Expected pick within a single round
  * 3 - The team that is expected to draft the player
  * 4 - The player's name
  * 5 - The player's position
  * 6 - The college the player attended
  * 7 - Ignore this column
  * 8 - Notes about the players
* All data in a given row relates to the player identified in column `2`.

`2025-nfl-dot-com-1st-round.csv`
* This file contains NFL.com's analysis of the first rounds picks in the NFL draft.
* Column Details
  * 1 - Overall expected pick (across all rounds of the draft)
  * 2 - Expected pick within a single round
  * 3 - The team that is expected to draft the player
  * 4 - The player's name
  * 5 - The player's position
  * 6 - The college the player attended
  * 7 - Ignore this column
  * 8 - Notes about the players
* All data in a given row relates to the player identified in column `2`.

`2025-pff-7-rounds.csv`
* This file contains Pro Football Focus's analysis of all seven rounds of the NFL draft.
* Not that many rookies with a potential impact will be drafted in the first round, so we need to also consider rounds 2 - 7.
  * Column Details
  * 1 - Overall expected pick (across all rounds of the draft)
  * 2 - Expected pick within a single round
  * 3 - The team that is expected to draft the player
  * 4 - The player's name
  * 5 - The player's position
  * 6 - The college the player attended
  * 7 - Ignore this column
  * 8 - Notes about the players (only the first three rounds feature notes about players)
* All data in a given row relates to the player identified in column `2`.
