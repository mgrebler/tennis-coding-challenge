from unittest import TestCase

from mock import patch, mock

from tennis_calculator_app import process_query, get_tournament_results


class TennisCalculator(TestCase):

    @patch('sys.stdout')
    def test_simple_game_query(self, mock_stdout):
        results = get_tournament_results(['test/test_data/simple_game.txt'])
        process_query('Games Player Person A', results)

        expout = "2 0"
        mock_stdout.write.assert_has_calls([
            mock.call(expout)
        ])


    @patch('sys.stdout')
    def test_simple_match_query(self, mock_stdout):
        results = get_tournament_results(['test/test_data/simple_game.txt'])
        process_query('Score Match 01', results)

        expout = """Incomplete game: Person A vs Person B
0 sets to 0
"""
        mock_stdout.write.assert_has_calls([
            mock.call(expout)
        ])

    @patch('sys.stdout')
    def test_complex_game_query(self, mock_stdout):
        results = get_tournament_results(['test/test_data/full_tournament.txt'])
        process_query('Games Player Person B', results)

        expout = "0 12"
        mock_stdout.write.assert_has_calls([
            mock.call(expout)
        ])
