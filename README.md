# NHL_PCA
Run a PCA (Principal Component Analysis) algorithm on a set of advanced NHL statistics.

Data Source: https://www.moneypuck.com/stats.htm

The following shows the top 10 advanced statistics that contribute towards PC1 and their loading scores.



Results:

timeOnBench :  0.896713331996098

icetime :  0.4415248677565037

OffIce_A_shotAttempts :  0.013460801650499458

OffIce_F_shotAttempts :  0.01285374173739825

shifts :  0.008855742695073707

I_F_shifts :  0.00885574269507369

OnIce_F_scoreAdjustedShotsAttempts :  0.0072250862244140545

OnIce_F_shotAttempts :  0.007193061525410129

OnIce_A_scoreAdjustedShotsAttempts :  0.00619648449922037

OnIce_A_shotAttempts :  0.006195625978162537



Key:

timeOnBench :  Amount of time the player has been on the bench for. (in seconds)

icetime :  Ice time in seconds

OffIce_A_shotAttempts :  Shot attempts AGAINST off the ice

OffIce_F_shotAttempts :  Shot attempts FOR off the ice

shifts :  Number of shifts a player had

I_F_shifts :  Number of shifts a player had

OnIce_F_scoreAdjustedShotsAttempts :  Score adjusted shot attempts FOR on the ice

OnIce_F_shotAttempts :  Shot attempts FOR on the ice

OnIce_A_scoreAdjustedShotsAttempts :  Score adjusted shot attempts AGAINST on the ice

OnIce_A_shotAttempts :  Shot attempts AGAINST on the ice



Conclusion:

PCA is meant to show which variables in a large set of variables demonstrate the most variation in the data. These statistics shown above represent the 10 variables that demonstrate the most variation in player's statistics across the league. Statistics like timeOnBench, icetime, and shifts are expected to be very high on this list because obviously better players are by default going to get more playing time; independent of if they are playing well or not. Therefor, because this data includes all players and not just the superstars of the league, there is going to be a lot of variation in those statistics. The other statistics all focus around shot attempts on/off the ice and for/against their teams. It is worthy to note that these shot attempt metrics are not isolated to just the player's shot attempt, but rather they include shot attempts by that player's linemates as well. Keeping this in mind, it make sense that better players can seperate themselves from other players by looking at the volume of shots their team produces while they're on the ice versus off the ice. This shows they even if they aren't the ones shooting the puck, they are still creating chances as well for their teammates.
