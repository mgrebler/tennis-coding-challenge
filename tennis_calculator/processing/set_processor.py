from tennis_calculator.processing import game_processor
from tennis_calculator.results.results import SetResult


def process_set(points):
    remaining_points = points

    g0 = 0
    g1 = 0
    game_results = []

    while remaining_points:

        if g0 == 6 and g1 == 6:
            return _handle_tiebreaker(remaining_points, game_results)

        result, remaining_points = game_processor.process_game(remaining_points)
        game_results.append(result)

        if result.winner == 0:
            g0 += 1

        if result.winner == 1:
            g1 += 1

        if abs(g0 - g1) > 1:
            if g0 >= 6 or g1 >= 6:
                return SetResult(result.winner, g0, g1, game_results), remaining_points

    return SetResult(None, g0, g1, game_results), remaining_points


def _handle_tiebreaker(points, game_results):
    result, remaining_points = game_processor.process_tiebreaker(points)
    game_results.append(result)

    if result.winner == 0:
        return SetResult(0, 7, 6, game_results), remaining_points

    if result.winner == 1:
        return SetResult(1, 6, 7, game_results), remaining_points

