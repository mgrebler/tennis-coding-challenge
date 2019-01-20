from tennis_calculator import set_processor
from tennis_calculator.results.results import MatchResult


class MatchProcessor:
    max_sets = 0

    def __init__(self, max_sets):
        self.max_sets = max_sets

    def process_match(self, points):
        remaining_points = points

        s0 = 0
        s1 = 0

        while remaining_points:

            if s0 == self.max_sets - 1 and s1 == self.max_sets - 1:
                result, remaining_points = set_processor.process_final_set(remaining_points)
            else:
                result, remaining_points = set_processor.process_set(remaining_points)

            if result.winner == 0:
                s0 += 1
            if result.winner == 1:
                s1 += 1

            if s0 == self.max_sets or s1 == self.max_sets:
                return MatchResult(result.winner, s0, s1)

        return MatchResult(None, s0, s1)


def process_womens_match(points):
    return process_womens_match.match_processor.process_match(points)

process_womens_match.match_processor = MatchProcessor(2)
