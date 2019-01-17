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

    Match 01
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

## Queries

TODO
* Who won more games between

## Rules
