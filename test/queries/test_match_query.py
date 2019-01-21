from unittest import TestCase

from tennis_calculator.queries.match_query import query_match
from tennis_calculator.results.results import NamedMatchResult, MatchResult, SetResult


class TestMatchQuery(TestCase):

    def test_player_0_wins(self):
        match = "01"

        set_results = [ SetResult(0, 6, 0, []), SetResult(1, 1, 6, []), SetResult(0, 6, 2, [])]
        match_result = MatchResult(0, 2, 1, set_results)
        results = {match: NamedMatchResult(match, "p1", "p2", match_result) }

        output = query_match(match, results)

        expected = """p1 defeated p2
2 sets to 1
6 0
1 6
6 2
"""
        self.assertEqual(expected, output)

    def test_player_1_wins(self):
        match = "01"

        set_results = [ SetResult(1, 0, 6, []), SetResult(0, 6, 1, []), SetResult(1, 2, 6, [])]
        match_result = MatchResult(1, 1, 2, set_results)
        results = {match: NamedMatchResult(match, "p1", "p2", match_result) }

        output = query_match(match, results)

        expected = """p2 defeated p1
2 sets to 1
6 0
1 6
6 2
"""
        self.assertEqual(expected, output)

    def test_game_incomplete(self):
        match = "01"

        set_results = [ SetResult(None, 1, 0, [])]
        match_result = MatchResult(None, 0, 0, set_results)
        results = {match: NamedMatchResult(match, "p1", "p2", match_result) }

        output = query_match(match, results)

        expected = """Incomplete game: p1 vs p2
0 sets to 0
1 0
"""
        self.assertEqual(expected, output)

    def test_not_found_game(self):
        match = "01"

        self.assertRaises(ValueError, query_match, match, {})


    def create_set_results(self, results):

        def winner(p0, p1):
            if p0 > p1:
                return 0
            return 1

        list(map(lambda x: SetResult(winner(x[0],x[1]), x[0], x[1], [])))
