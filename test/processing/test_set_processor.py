from unittest import TestCase
import mock

from tennis_calculator.processing import game_processor
from tennis_calculator.processing.set_processor import process_set, process_final_set
from tennis_calculator.results.results import GameResult, SetResult

P0_GAME = (GameResult(0, 4, 1), [1])
P1_GAME = (GameResult(1, 0, 4), [1])

class TestSetProcessor(TestCase):

    def setUp(self):
        self.tmp_process_game = game_processor.process_game
        self.tmp_process_tiebreaker = game_processor.process_tiebreaker
        game_processor.process_game = mock.Mock()
        game_processor.process_tiebreaker = mock.Mock()

    def tearDown(self):
        game_processor.process_game = self.tmp_process_game
        game_processor.process_tiebreaker = self.tmp_process_tiebreaker

    def test_p0_wins(self):

        game_processor.process_game.side_effect = [P0_GAME] * 6

        result, _ = process_set([0])

        self.assertEqual(0, result.winner)

    def test_p1_wins(self):

        game_processor.process_game.side_effect = [P1_GAME] * 6

        result, _ = process_set([0])

        self.assertEqual(1, result.winner)

    def test_scores_correct(self):

        game_processor.process_game.side_effect = [P0_GAME] + [P1_GAME] * 6

        result, _ = process_set([0])

        self.assertEqual(1, result.person_0_games)
        self.assertEqual(6, result.person_1_games)

    def test_game_results_stored(self):

        game_results_with_remaining_points = [P0_GAME] + [P1_GAME] * 6
        game_processor.process_game.side_effect = game_results_with_remaining_points

        result, _ = process_set([0])

        expected_game_results = list(map(lambda x: x[0], game_results_with_remaining_points))

        self.assertEqual(expected_game_results, result.game_results)

    def test_7_5_game(self):

        game_processor.process_game.side_effect = \
            [P0_GAME] * 5 + [P1_GAME] * 5 + [P0_GAME] * 2

        result, _ = process_set([0])

        self.assertEqual(0, result.winner)
        self.assertEqual(7, result.person_0_games)
        self.assertEqual(5, result.person_1_games)


    def test_tie_break_p0_win(self):

        game_processor.process_game.side_effect = \
            [P0_GAME] * 5 + [P1_GAME] * 6 + [P0_GAME]

        game_processor.process_tiebreaker.return_value = P0_GAME

        result, _ = process_set([0])

        self.assertEqual(0, result.winner)
        self.assertEqual(7, result.person_0_games)
        self.assertEqual(6, result.person_1_games)

    def test_tie_break_p1_win(self):

        game_processor.process_game.side_effect = \
            [P0_GAME] * 5 + [P1_GAME] * 6 + [P0_GAME]

        game_processor.process_tiebreaker.return_value = P1_GAME

        result, _ = process_set([0])

        self.assertEqual(1, result.winner)
        self.assertEqual(6, result.person_0_games)
        self.assertEqual(7, result.person_1_games)


    def test_incomplete_set(self):

        game_result = GameResult(0, 4, 0)
        game_processor.process_game.return_value = (game_result, [])

        result, remaining = process_set([0])

        self.assertEqual(SetResult(None, 1, 0, [game_result]), result)
        self.assertFalse(remaining)

    def test_incomplete_game_within_a_set(self):

        game_result = GameResult(None, 1, 0)
        game_processor.process_game.return_value = (game_result, [])

        result, remaining = process_set([0])

        self.assertEqual(SetResult(None, 0, 0, [game_result]), result)
        self.assertFalse(remaining)

    def test_final_set(self):

        game_processor.process_game.side_effect = \
            [P0_GAME] * 5 + [P1_GAME] * 6 + [P0_GAME, P1_GAME, P1_GAME]

        result, _ = process_final_set([0])

        self.assertEqual(1, result.winner)
        self.assertEqual(6, result.person_0_games)
        self.assertEqual(8, result.person_1_games)

