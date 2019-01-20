# Tennis Calculator

The tennis calculator takes a set of scores as inputs and produces useful staticstics based on those scores.

## Overview

The Tennis Calculator takes inputs in the form of a list of points of a tennis match. 

Given this list of points, it will calculate the "games", "sets" and "matches" results.

From there it can be queried about various statictics around the input matches it received. 
For example:
* Who won the most matches
* What was the result of a particular match
* Which game went for the most points

## Input

The input will have some header lines, and then a list of points. 
For example, the following would result in 2 games to "Person A":

    Match: 01
    Person A vs Person B
    0
    1
    0
    1
    0
    0

    0
    0
    0
    0

    
The first row is a match id, the second row shows who is playing against whom.
After that are a series of points, where 0 is a point for the first person listed, 1 is for last person.


In the example above, a blank line is used to indicate the end of a game.

For processing, blank lines must be ignored, and can **not** be relied upon to indicate the completion of the game

## Queries

### Query match result
Query scores for a particular match
Prints who defeated whom, and the result of the sets for the match (winning player score first).

Query: `Score Match <id>`

Example: `Score Match 01`

Example output:

    Person A defeated Person B
    6 1
    4 6
    8 6
 
### Query tournament summary results
Prints the sorted ladder for the tournament. On each line it shows:
* Number of match wins
* Number of match losses
* Number of "no result" matches.


Query: `Tournament summary`

Example output:

    4 0 0 Person A
    3 1 0 Person B
    2 1 1 Person C
    2 2 0 Person D
    0 0 1 Person E
    0 1 1 Person F


### Query games for player
Prints a summary of games won vs lost for a particular player over the tournament
Query: `Games Player <Player Name>`

Example: `Games Player Person A`

Example output:

    37 56

## Scoring Rules
Details of tennis scoring can be found online. 
The variation used for this application is that used in the Australian Open. 
i.e. 
* Advantage scoring for games (after deuce must win by two points)
* First to 2 sets (Women's games only)
* Tie breaks when sets are 6-6 (except deciding set)
   * Tie breaks played to 7 points with advantage (must win by 2)
* In the deciding set, games continue to play as normal without tie breaker until someone wins by 2 games.

