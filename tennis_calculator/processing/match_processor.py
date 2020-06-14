from tennis_calculator.processing import set_processor
from tennis_calculator.results.results import MatchResult


class MatchProcessor:
    max_sets = 0

    def __init__(self, max_sets):
        self.max_sets = max_sets

    def process_match(self, points):
        remaining_points = points
        set_results = []

        s0 = 0
        s1 = 0

        while remaining_points:

            result, remaining_points = set_processor.process_set(remaining_points)

            set_results.append(result)

            if result.winner == 0:
                s0 += 1
            if result.winner == 1:
                s1 += 1

            if s0 == self.max_sets or s1 == self.max_sets:
                return MatchResult(result.winner, s0, s1, set_results)

        return MatchResult(None, s0, s1, set_results)


def process_womens_match(points):
    return process_womens_match.match_processor.process_match(points)

process_womens_match.match_processor = MatchProcessor(2)
