# Readme for interviewer issuing the challenge
Note: This file should **NOT** be sent to the interviewee.

# Preparation

* Switch to `pairing_challenge` branch
    * This branch has the new functionality from what the received initially
    * The `point_query` functionality does not exist in `master`
* **Remove** 
    * The "instructions" directory 
    * The .git directory 
* Zip up what's left 
* Send the zip to the candidate just before the start of the pairing challenge
* Get them to unzip the new code and get it running again
* Print out these notes for the interviewer
* Print out `02_4_README_pairing_challenge_questions.md` for the interviewee  

# Scenario

The scenario is that we (interviewee and interviewer) have been asked to get this toy, non-production code ready for production.

# Notes for the interviewer

## Before question 1 (approx 5 min)
Ask how they went with their at-home warm-up challenge. 

1. Did they find the bug in `match_processor.py`
    * i.e. It should be:
    * `if s0 == self.max_sets - 1 and s1 == self.max_sets:`
1. Did they add update or add any tests for that functionality?
    * E.g. `test_match_processor.py` could check if `process_final_set` is called
    * E.g.2. `test_tennis_calculator_app.py` could use `full_tournament.txt`

## Question 1 Notes (approx 20 min)
A bug has been introduced in `game_processor.py`

    return GameResult(None, p0, 1), points

Should be:

    return GameResult(None, p0, p1), points


Note that if they spend too much time looking in `point_query.py`, hint that the bug may have been introduced elsewhere.


* After finding the bug, do they create a failing test (or fix the broken test)?
   * Do they create the test before fixing the code?
* Does the interviewer refactor anything on the way (or after finding and fixing the bug)?
   * If they do refactor, do they ensure that RuleFactoryTest has adequate coverage first?
   * It's not essential that they do refactor at this stage 
   (although some might do so just to make the code understandable, which you can encourage), 
   but take note of if they mention that it should be refactored given that it's going into 
   production.


## Question 2 Notes (approx 40 min)
* How do they go about creating the new functionality?
   * What questions do they ask about the output?
   * Do they create tests first?
   * What does their code look like?

## Question 3 Notes (approx 20 min)

**Part A:** 
* What questions / assumptions do they have around the level of code quality for "production"?
* How do they look over the codebase to find things that need cleanup?
* What do they identify that needs cleanup?

**Part B:**
* Do they ensure that `tennis_calculator_app.py` has adequate coverage first?
* How clean do they make it? 
* How small do they split up the methods?

## Finally (5 min)
Any other questions from the candidate?
