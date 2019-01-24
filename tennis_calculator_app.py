import argparse
import sys

from tennis_calculator.queries.game_query import get_player_name, query_games
from tennis_calculator.queries.match_query import get_match_id, query_match
from tennis_calculator.processing import match_processor
from tennis_calculator.results.results import NamedMatchResult


def main(args):
    tournament_results = get_tournament_results(args)
    process_queries(tournament_results)


def get_tournament_results(args):
    score_file = get_score_file(args)
    tournament_results = parse_tournament(score_file)
    return tournament_results


def get_score_file(args):
    parser = argparse.ArgumentParser(description="The tennis calculator takes a set of scores as inputs and produces "
                                                 "useful statistics based on those scores.")
    parser.add_argument('score_file', type=argparse.FileType('r'),
                        help='A file containing multiple tennis matches')

    return parser.parse_args(args).score_file


def process_queries(tournament_results):
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        process_query(line, tournament_results)


def process_query(line, results):
    player = get_player_name(line)
    match = get_match_id(line)

    if player:
        print query_games(player, results)
    elif match:
        print query_match(match, results)
    else:
        print "Unrecognised query: %s" % line


def parse_tournament(score_file):
    r, m, p0, p1, p = {}, None, None, None, [] # results, match, points, player 0, player 1

    for l in score_file:
        l_ = l.strip()

        lt = get_line_type(l_, m, p0)

        if lt == "1st match line":
            # check for the first match line.
            if l_.find("Match: ") == 0:
                m = l_[7:]
            else:
                # Raise value error if we don't find a match id
                raise ValueError("Expected Match but found line: %s" % l_)
        elif lt == "player line":
            # Check for player vs player line
            i = l_.find(" vs ")
            if i > -1:
                p0 = l_[:i]
                p1 = l_[(i + 4):]
            else:
                # Raise value error if don't match player
                raise ValueError("Expected player names but found line: %s" % l_)
        elif lt == "player 0 point":
            p.append(0)
        elif lt == "player 1 point":
            p.append(int(l_))
        elif lt == "blank line":
            # Ignore blank lines
            continue
        elif lt == "match line":
            r[m] = NamedMatchResult(m, p0, p1, match_processor.process_womens_match(p))
            # Check for player vs player line
            if l_.find("Match: ") == 0:
                m = l_[len("Match: "):]
            else:
                # Raise value error if don't match player
                raise ValueError("Expected Match but found line: %s" % l_)

            p0, p1 = None, None

            p = []

    r[m] = NamedMatchResult(m, p0, p1, match_processor.process_womens_match(p))

    return r


def get_line_type(l_, m, p0):
    if not m:
        lt = "1st match line"
    elif not p0:
        lt = "player line"
    elif l_ == "0":
        lt = "player 0 point"
    elif l_ == "1":
        lt = "player 1 point"
    elif not l_:
        lt = "blank line"
    else:
        lt = "match line"
    return lt



if __name__ == "__main__":
    main(sys.argv[1:])
