from unittest import TestCase

from mock import patch, mock

from tennis_calculator_app import process_query, get_tournament_results


class TennisCalculator(TestCase):

    @patch('sys.stdout')
    def test_simple_game_query(self, mock_stdout):
        results = get_tournament_results(['test_data/simple_game.txt'])
        process_query('Games Player Person A', results)

        expout = "2 0"
        mock_stdout.write.assert_has_calls([
            mock.call(expout)
        ])


    @patch('sys.stdout')
    def test_simple_match_query(self, mock_stdout):
        results = get_tournament_results(['test_data/simple_game.txt'])
        process_query('Score Match 01', results)

        expout = """Incomplete game: Person A vs Person B
0 sets to 0
2 0
"""
        mock_stdout.write.assert_has_calls([
            mock.call(expout)
        ])

    @patch('sys.stdout')
    def test_complex_game_query(self, mock_stdout):
        results = get_tournament_results(['test_data/full_tournament.txt'])
        process_query('Games Player Person A', results)

        expout = "27 18"
        mock_stdout.write.assert_has_calls([
            mock.call(expout)
        ])


    @patch('sys.stdout')
    def test_complex_match_query(self, mock_stdout):
        results = get_tournament_results(['test_data/full_tournament.txt'])
        process_query('Score Match 02', results)

        expout = """Person A defeated Person C
2 sets to 1
7 6
0 6
8 6
"""
        mock_stdout.write.assert_has_calls([
            mock.call(expout)
        ])
