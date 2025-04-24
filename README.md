# 2025 LFFL Draft Research

## Instructions
When doing any sort of analysis, always follow these general rules:
1. `2025-my-active-roster.csv` should be used to learn about my current team roster.
2. `2025-fantasy-pros-rookie-rankings.csv` should always be used to determine the most probable draft posistion for each player in the LFFL draft.
3. Use `2025-mel-kiper -1st-round.csv`, `2025-nfl-dot-com-1st-round.csv`, `2025-pff-1st-round.csv`, and `2025-fantasy-pros-1st-round-with-trades.csv` to determine how actual draft position might rise or fall from the order provided in `2025-fantasy-pros-rookie-rankings.csv`.
4. Use `




2025-my-active-roster.csv





* Always use the following files when doing any analysis:
  * 2025-roster-review(Active Roster Review).csv
  * 2025-roster-review(FP Rookie Rankings).csv
  * 2025-roster-review(PFF - 7 Rnds).csv
  * 2025-roster-review(NFL - 1 Rnd).csv
  * 2025-roster-review(Mel Kiper - 1 Rnd).csv
  * 2025-roster-review(FP - 1 Rnd (Trades)).csv
* When determining which players might still be available when making my picks, give the rankings found in `2025-roster-review(FP Rookie Rankings).csv` more weight than the other rankings.
* Always consider details about my team when analyzing the data, these details are found in the `2025-roster-review(Active Roster Review).csv`.
* In fantasy football we are only interested in QB, WR, RB, and TE
* The notes provided about each player should be aggregated and analyzed to identify potential sleepers
* A "sleeper" is a player that is picked later in the draft that is likely to outperform players picked before them

# Draft Details
* The rookie draft for my dynasty fantasy football league is 4 rounds long with 6 pick in each round
* I have the 5th, 7th, 17th, and 20th picks in the draft

# Description of files in the repository
2025-roster-review(Active Roster Review).csv
* This file contains a breakdown of my team.  The players are ranked by dynasty value.
* This file should be used as a basis when making decisions about who I should draft.
* Generally, this breakdown shows that I need to improve at wide receiver (WR) and tight end (TE); however, I strongly value running backs (RB) and if a good one is available I would probably take the RB over a TE and most likely over a WR unless the WR is very good.
* Column Details
  * A - Rank on my team (If this column does not have a number, that means the player is not on my team, but I have interest in them)
  * B - Player name
  * C - Dynasty Nerds ranking for the player for their specific position
  * D - Ignore this column
  * E - ESPN ranking for the player for their specific position
  * F - ESPN overall ranking for the player
  * G - PFF ranking for the player for their specific position
  * H - PFF overall ranking for the player
  * I - Ignore this column
  * J - FantasyPros ranking for the player for their specific position
  * K - FantasyPros overall ranking for the player
  * L - FantasyPros tier for that player for their specific position

2025-roster-review(FP Rookie Rankings).csv
* This file contains an ordered ranking of the rookies available in the 2025 NFL draft from a dynasty fantasy football perspective.
* Players are valued differently in fantasy football than they are in the real NFL.
* Fantasy football is only interested in quarterbacks (QB or Q), running backs (RB or HB), wide receivers (WR), and tight ends (TE).
* Column Details
  * A - Overall dynasty fantasy football rank for 2025 drafts
  * B - Player name
  * C - Position the player plays
  * D - Highest possible draft position
  * E - Lowest possible draft position
  * F - Average draft position
  * G - Standard deviation
* All data in a given row relates to the player identified in column `B`.

2025-roster-review(Mel Kiper - 1 Rnd).csv
* This file contains Mel Kiper's analysis of the first rounds picks in the NFL draft.
* Column Details
  * A - Overall expected pick (across all rounds of the draft)
  * B - Expected pick within a single round
  * C - The team that is expected to draft the player
  * D - The player's name
  * E - The player's position
  * F - The college the player attended
  * G - Ignore this column
  * H - Ignore this column
* All data in a given row relates to the player identified in column `D`.

2025-roster-review(FP - 1 Rnd (Trades)).csv
* This file contains Fantasy Pro's analysis of the first rounds picks in the NFL draft.
* For this mock draft, they took into consideration potential trades that NFL team might make.
* Column Details
  * A - Overall expected pick (across all rounds of the draft)
  * B - Expected pick within a single round
  * C - The team that is expected to draft the player
  * D - The player's name
  * E - The player's position
  * F - The college the player attended
  * G - Ignore this column
  * H - Notes about the players
* All data in a given row relates to the player identified in column `D`.

2025-roster-review(NFL - 1 Rnd).csv
* This file contains NFL.com's analysis of the first rounds picks in the NFL draft.
* Column Details
  * A - Overall expected pick (across all rounds of the draft)
  * B - Expected pick within a single round
  * C - The team that is expected to draft the player
  * D - The player's name
  * E - The player's position
  * F - The college the player attended
  * G - Ignore this column
  * H - Notes about the players
* All data in a given row relates to the player identified in column `D`.

2025-roster-review(PFF - 7 Rnds).csv
* This file contains Pro Football Focus's analysis of all seven rounds of the NFL draft.
* Not that many rookies with a potential impact will be drafted in the first round, so we need to also consider rounds 2 - 7.
  * Column Details
  * A - Overall expected pick (across all rounds of the draft)
  * B - Expected pick within a single round
  * C - The team that is expected to draft the player
  * D - The player's name
  * E - The player's position
  * F - The college the player attended
  * G - Ignore this column
  * H - Notes about the players (only the first three rounds feature notes about players)
* All data in a given row relates to the player identified in column `D`.
