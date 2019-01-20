from unittest import TestCase

from tennis_calculator.game_processor import GameProcessor, process_game, NORMAL_GAME_POINTS, \
    TIE_BREAK_POINTS, process_tiebreaker
from tennis_calculator.results.results import GameResult


class TestGameProcessor(TestCase):

    def setUp(self):
        self.game_processor = GameProcessor(4)

    def test_p0_wins(self):
        result, _ = self.game_processor.process_game([0,0,0,0])
        self.assertEqual(0, result.winner)

    def test_p1_wins(self):
        result, _ = self.game_processor.process_game([1,1,1,1])
        self.assertEqual(1, result.winner)

    def test_no_remaining_points_for_complete_game(self):
        _, remaining = self.game_processor.process_game([0,0,0,0])
        self.assertFalse(remaining)

    def test_scores(self):
        result, _ = self.game_processor.process_game([1,0,1,0,0,0])
        self.assertEqual(4, result.person_0_score)
        self.assertEqual(2, result.person_1_score)

    def test_advantage_win(self):
        result, _ = self.game_processor.process_game([1,0,1,0,1,0,1,1])
        self.assertEquals(GameResult(1,3,5), result)

    def test_remaining_games(self):
        _, remaining = self.game_processor.process_game([0,0,0,0,1,0])
        self.assertListEqual([1,0], remaining)

    def test_incomplete_game(self):
        result, _ = self.game_processor.process_game([0,0,0])
        self.assertEquals(GameResult(None,3,0), result)

    def test_invalid_input(self):
        self.assertRaises(ValueError, self.game_processor.process_game, [2])

    def test_handles_regular_game(self):
        result, remaining = process_game([0] * NORMAL_GAME_POINTS)
        self.assertEqual(0, result.winner)
        self.assertFalse(remaining)

    def test_handles_tie_breaker(self):
        result, remaining = process_tiebreaker([0] * TIE_BREAK_POINTS)
        self.assertEqual(0, result.winner)
        self.assertFalse(remaining)
