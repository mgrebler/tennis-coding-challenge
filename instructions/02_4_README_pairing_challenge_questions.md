
We (interviewee and interviewer) have been asked to get this toy, non-production code ready for production.

# Question 1
There seems to be a bug in the application.

Running the application using against the 'full_tournament.txt' file results in the following:

    $ python tennis_calculator_app.py test/test_data/full_tournament.txt
    Points Player Person A

Should result in 

    `115 82`

But does not. Instead it results in:

    `115 81`


Please diagnose and fix the bug properly.

# Question 2

Now we need to enhance the functionality for our MVP. 

We need to add a new query:
### Query tournament summary results
Prints a summary list for all of the players in the tournament (sorted by player name). On each line it shows:
* Player name
* Number of match wins
* Number of match losses
* Number of "no result" matches.


Query: `Tournament summary`

Example output:

    Person A 4 0 0 
    Person B 0 1 0
    Person C 2 1 1

# Question 3

Now we've fixed the bugs and have an MVP, is there any cleaning up we need to do to get this production ready?

**Part A:** At a high level, what cleaning up is needed? Please take some notes on the work required.

**Part B:** Ok, let's cleanup `tennis_calculator_app.py` together, which is a bit of a basket case.
