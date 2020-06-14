import tempfile
from unittest import TestCase

import mock

from tennis_calculator.processing import match_processor
from tennis_calculator.results.results import NamedMatchResult, MatchResult
from tennis_calculator_app import parse_tournament

MATCH_RESULT = MatchResult(0, 2, 0, [])

class TestTournamentParser(TestCase):

    def setUp(self):
        self.tmp_process_womens_match = match_processor.process_womens_match
        match_processor.process_womens_match = mock.Mock()
        self.input_file = tempfile.SpooledTemporaryFile(10 ** 9, "w")

    def tearDown(self):
        match_processor.process_womens_match = self.tmp_process_womens_match

    def set_tournament_content(self, content):
        self.input_file.write(content)
        self.input_file.seek(0)
        return self.input_file

    def test_parses_single_match(self):
        match_processor.process_womens_match.return_value = MATCH_RESULT
        file = self.set_tournament_content(
            """Match: 01
            Player A vs Player B
            0
            """
        )

        result = parse_tournament(file)
        expected = { "01": NamedMatchResult("01", "Player A", "Player B", MATCH_RESULT) }
        self.assertEqual(expected, result)

    def test_parses_multiple_matches(self):
        match_processor.process_womens_match.return_value = MATCH_RESULT
        file = self.set_tournament_content(
            """Match: 01
            Player A vs Player B
            0
            Match: 02
            Player C vs Player D
            0
            """
        )

        result = parse_tournament(file)
        expected = { "01": NamedMatchResult("01", "Player A", "Player B", MATCH_RESULT),
                     "02": NamedMatchResult("02", "Player C", "Player D", MATCH_RESULT) }
        self.assertEqual(expected, result)

    def test_invalid_match(self):
        file = self.set_tournament_content(
            """
            INVALID
            """
        )
        self.assertRaises(ValueError, parse_tournament, file)

    def test_invalid_players(self):
        file = self.set_tournament_content(
            """
            Match: 01
            INVALID
            """)
        self.assertRaises(ValueError, parse_tournament, file)
