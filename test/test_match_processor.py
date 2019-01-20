from unittest import TestCase

import mock

from tennis_calculator import set_processor
from tennis_calculator.match_processor import MatchProcessor, MatchResult
from tennis_calculator.set_processor import SetResult

P0_SET = SetResult(0, 6, 0), [0]
P1_SET = SetResult(1, 0, 6), [0]

class TestMatchProcessor(TestCase):

    def setUp(self):
        self.tmp_process_set = set_processor.process_set
        self.tmp_process_final_set = set_processor.process_final_set
        set_processor.process_final_set = mock.Mock()

        self.match_processor = MatchProcessor(3)

    def tearDown(self):
        set_processor.process_set = self.tmp_process_set
        set_processor.process_final_set = self.tmp_process_final_set

    def test_p0_wins(self):

        set_processor.process_set.side_effect = [P0_SET] * 3

        result, _ = self.match_processor.process_match([0])

        self.assertEqual(0, result.winner)

    def test_p1_wins(self):

        set_processor.process_set.side_effect = [P1_SET] * 3

        result, _ = self.match_processor.process_match([0])

        self.assertEqual(1, result.winner)

    def test_score(self):

        set_processor.process_set.side_effect = [P0_SET] + [P1_SET] * 3

        result, _ = self.match_processor.process_match([0])

        self.assertEqual(MatchResult(1,1,3), result)

    def test_final_set(self):

        set_processor.process_set.side_effect = [P0_SET] * 2 + [P1_SET] * 2
        set_processor.process_final_set.side_effect = [P0_SET]

        result, _ = self.match_processor.process_match([0])

        self.assertEqual(MatchResult(0,3,2), result)

    def test_incomplete_match(self):
        set_processor.process_set.return_value = (SetResult(None, 1 ,0), [])

        result, remaining = self.match_processor.process_match([0])

        self.assertEqual(SetResult(None, 1, 0), result)
        self.assertFalse(remaining)
