from unittest import TestCase

from tennis_calculator.queries.game_query import query_games
from tennis_calculator.results.results import SetResult, MatchResult, NamedMatchResult


class TestGameQuery(TestCase):

    def test_prints_games_for_player(self):

        set_results_1 = [ SetResult(0, 6, 0, []), SetResult(1, 1, 6, []), SetResult(0, 6, 2, [])]
        match_result_1 = MatchResult(0, 2, 1, set_results_1)

        set_results_2 = [ SetResult(None, 1, 1, [])]
        match_result_2 = MatchResult(None, 0, 0, set_results_2)

        p1 = "p1"
        results = { "01": NamedMatchResult("01", p1, "p2", match_result_1),
                    "02": NamedMatchResult("02", p1, "p3", match_result_2)}

        expected = "14 9"

        output = query_games(p1, results)

        self.assertEqual(expected, output)

    def test_prints_nothing_when_no_player(self):

        p1 = "p1"
        results = { }

        expected = "0 0"

        output = query_games(p1, results)

        self.assertEqual(expected, output)