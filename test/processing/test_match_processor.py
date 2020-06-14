from unittest import TestCase

import mock

from tennis_calculator.processing import set_processor
from tennis_calculator.processing.match_processor import MatchProcessor
from tennis_calculator.results.results import SetResult, MatchResult

P0_SET = SetResult(0, 6, 0, []), [0]
P1_SET = SetResult(1, 0, 6, []), [0]
P0_FINISH_SET = SetResult(0, 6, 0, []), []
P1_FINISH_SET = SetResult(1, 0, 6, []), []

class TestMatchProcessor(TestCase):

    def setUp(self):
        self.tmp_process_set = set_processor.process_set
        set_processor.process_set = mock.Mock()

        self.match_processor = MatchProcessor(3)

    def tearDown(self):
        set_processor.process_set = self.tmp_process_set

    def test_p0_wins(self):

        set_processor.process_set.side_effect = [P0_SET] * 2 + [P0_FINISH_SET]

        result = self.match_processor.process_match([0])

        self.assertEqual(0, result.winner)

    def test_p1_wins(self):

        set_processor.process_set.side_effect = [P1_SET] * 2 + [P1_FINISH_SET]

        result = self.match_processor.process_match([0])

        self.assertEqual(1, result.winner)

    def test_score(self):

        set_processor.process_set.side_effect = [P0_SET] + [P1_SET] * 2 + [P1_FINISH_SET]

        result = self.match_processor.process_match([0])

        self.assertEqual(1, result.person_0_sets)
        self.assertEqual(3, result.person_1_sets)

    def test_set_results(self):

        set_results_with_points = [P0_SET] + [P1_SET] * 2 + [P1_FINISH_SET]
        set_processor.process_set.side_effect = set_results_with_points

        result = self.match_processor.process_match([0])

        expected = list(map(lambda x: x[0], set_results_with_points))

        self.assertEqual(expected, result.set_results)

    def test_final_set(self):

        set_processor.process_set.side_effect = [P0_SET] * 2 + [P1_SET] * 2 + \
                                                [P1_FINISH_SET]

        result = self.match_processor.process_match([0])

        self.assertEqual(1, result.winner)
        self.assertEqual(2, result.person_0_sets)
        self.assertEqual(3, result.person_1_sets)

    def test_incomplete_match(self):
        set_processor.process_set.return_value = P0_FINISH_SET

        result = self.match_processor.process_match([0])

        self.assertEqual(MatchResult(None, 1, 0, [P0_FINISH_SET[0]]), result)

    def test_complete_match_ignores_excess_points(self):
        set_processor.process_set.side_effect = [P0_SET] * 3

        result = self.match_processor.process_match([0])

        self.assertEqual(3, result.person_0_sets)

