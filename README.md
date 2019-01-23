TODO
- sample file with input and expected output.
- Fully specify the scoring system.
- Remove Tournament summary query?

# Tennis Calculator

The tennis calculator takes a set of scores as inputs and produces useful statistics based on those scores.

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
For example:, the following would result in 2 games to "Person A":

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


For processing, blank lines must be ignored

## Queries

### Query match result
Query scores for a particular match
Prints who defeated whom, and the result of the sets for the match (winning player score first).

Query: `Score Match <id>`

Example: `Score Match 01`

Example output:

    Person A defeated Person B
    2 sets to 1
    6 1
    4 6
    8 6
 
### Query games for player
Prints a summary of games won vs lost for a particular player over the tournament
Query: `Games Player <Player Name>`

Example: `Games Player Person A`

Example output:

    37 56

## Sample output
Running the application against the 'full_tournament.txt' file results in the following:

    $ python tennis_calculator_app.py test/test_data/full_tournament.txt << EOF
    Score Match 02
    Games Player Person A
    EOF
    
    Person A defeated Person C
    2 sets to 1
    7 6
    0 6
    8 6
    
    27 18
    


## Scoring Rules
Details of tennis scoring can be found online. See here for reference:  
https://en.wikipedia.org/wiki/Tennis_scoring_system
The variation used for this application is that used in the Australian Open. 
A brief summary is as follows:
* A tennis match is split up into points, games and sets.
* Winning a game requires a person to win 4 points, but they must be ahead by at least 2 points (deuce, advantage, game)
* The first player to win 6 games wins a set, but:
    * They must be ahead by 2, unless the set goes to 6 games each, then a tiebreak will be played
    * A tiebreak is a special game which is the first person to get to 7 points, with at least 2 points ahead
* First to 2 sets (Women's games only) wins.
* In the deciding set (if the players get to 1 set each), games continue to play as normal without tie breaker until someone wins by 2 games.

