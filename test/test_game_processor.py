from unittest import TestCase

from tennis_calculator.game_processor import process_game, GameResult


class TestGameProcessor(TestCase):

    def test_p0_wins(self):
        result = process_game([0,0,0,0])
        self.assertEqual(result.winner, 0)

    def test_p1_wins(self):
        result = process_game([1,1,1,1])
        self.assertEqual(result.winner, 1)

    def test_no_remaining_points_for_complete_game(self):
        result = process_game([0,0,0,0])
        self.assertFalse(result.remaining_points)

    def test_scores(self):
        result = process_game([1,0,1,0,0,0])
        self.assertEqual(result.person_0_score, 4)
        self.assertEqual(result.person_1_score, 2)

    def test_advantage_win(self):
        result = process_game([1,0,1,0,1,0,1,1])
        self.assertEquals(result, GameResult(1,3,5,[]))

    def test_remaining_games(self):
        result = process_game([0,0,0,0,1,0])
        self.assertListEqual(result.remaining_points, [1,0])

    def test_invalid_input(self):
        self.assertRaises(ValueError, process_game, [2])
