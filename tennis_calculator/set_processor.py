from collections import namedtuple

from tennis_calculator import game_processor

from tennis_calculator.game_processor import process_game

SetResult = namedtuple('SetResult', ['winner', 'person_0_games', 'person_1_games'])


def handle_tiebreaker(points):
    result, remaining_points = game_processor.process_tiebreaker(points)

    if result.winner == 0:
        return SetResult(0, 7, 6), remaining_points

    if result.winner == 1:
        return SetResult(1, 6, 7), remaining_points


def process_set(points):
    remaining_points = points

    g0 = 0
    g1 = 0

    while remaining_points:

        if g0 == 6 and g1 == 6:
            return handle_tiebreaker(remaining_points)

        result, remaining_points = game_processor.process_game(remaining_points)

        if result.winner == 0:
            g0 += 1

        if result.winner == 1:
            g1 += 1

        if abs(g0 - g1) > 1:

            if g0 >= 6:
                return SetResult(0, g0, g1), remaining_points

            if g1 >= 6:
                return SetResult(1, g0, g1), remaining_points

    return SetResult(None, g0, g1), remaining_points