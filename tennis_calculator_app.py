import argparse
import sys

from tennis_calculator.processing.tournament_parser import *
from tennis_calculator.queries.game_query import get_player_name, query_games
from tennis_calculator.queries.match_query import get_match_id, query_match


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


if __name__ == "__main__":
    main(sys.argv[1:])
