from unittest import TestCase
import mock

from tennis_calculator import game_processor
from tennis_calculator.game_processor import GameResult
from tennis_calculator.set_processor import process_set, SetResult


class TestGameProcessor(TestCase):



    def test_p0_wins(self):

        game_processor.process_game = mock.Mock()
        game_processor.process_game.side_effect = [
            (GameResult(0, 4 ,0), [1]),
            (GameResult(0, 4 ,0), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(0, 4, 0), []),
        ]

        result, _ = process_set([0])

        self.assertEqual(result.winner, 0)

    def test_p1_wins(self):

        game_processor.process_game = mock.Mock()
        game_processor.process_game.side_effect = [
            (GameResult(1, 0 ,4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), []),
        ]

        result, _ = process_set([0])

        self.assertEqual(result.winner, 1)

    def test_scores_correct(self):

        game_processor.process_game = mock.Mock()
        game_processor.process_game.side_effect = [
            (GameResult(1, 0 ,4), [1]),
            (GameResult(0, 4 ,0), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), []),
        ]

        result, _ = process_set([0])

        self.assertEqual(result.person_0_games, 1)
        self.assertEqual(result.person_1_games, 6)

    def test_7_5_game(self):

        game_processor.process_game = mock.Mock()
        game_processor.process_game.side_effect = [
            (GameResult(0, 4 ,0), [1]),
            (GameResult(0, 4 ,0), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(1, 0 ,4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(0, 4, 0), [1]),
        ]

        result, _ = process_set([0])

        self.assertEqual(0, result.winner)
        self.assertEqual(result.person_0_games, 7)
        self.assertEqual(result.person_1_games, 5)


    def test_tie_break_p0_win(self):

        game_processor.process_game = mock.Mock()
        game_processor.process_tiebreaker = mock.Mock()


        game_processor.process_game.side_effect = [
            (GameResult(0, 4 ,0), [1]),
            (GameResult(0, 4 ,0), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(1, 0 ,4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(0, 4, 0), [1]),
        ]

        game_processor.process_tiebreaker.return_value = (GameResult(0, 7, 0), [])

        result, _ = process_set([0])

        self.assertEqual(0, result.winner)
        self.assertEqual(result.person_0_games, 7)
        self.assertEqual(result.person_1_games, 6)

    def test_tie_break_p1_win(self):

        game_processor.process_game = mock.Mock()
        game_processor.process_tiebreaker = mock.Mock()

        game_processor.process_game.side_effect = [
            (GameResult(0, 4 ,0), [1]),
            (GameResult(0, 4 ,0), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(0, 4, 0), [1]),
            (GameResult(1, 0 ,4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(1, 0, 4), [1]),
            (GameResult(0, 4, 0), [1]),
        ]

        game_processor.process_tiebreaker.return_value = (GameResult(1, 0, 7), [])

        result, _ = process_set([0])

        self.assertEqual(1, result.winner)
        self.assertEqual(result.person_0_games, 6)
        self.assertEqual(result.person_1_games, 7)


    def test_incomplete_set(self):

        game_processor.process_game = mock.Mock()
        game_processor.process_tiebreaker = mock.Mock()

        game_processor.process_game.return_value = (GameResult(0, 4 ,0), [])

        result, remaining = process_set([0])

        self.assertEqual(SetResult(None, 1, 0), result)
        self.assertFalse(remaining)

    def test_incomplete_game_within_a_set(self):

        game_processor.process_game = mock.Mock()
        game_processor.process_tiebreaker = mock.Mock()

        game_processor.process_game.return_value = (GameResult(None, 1 ,0), [])

        result, remaining = process_set([0])

        self.assertEqual(SetResult(None, 0, 0), result)
        self.assertFalse(remaining)
