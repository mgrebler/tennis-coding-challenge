import sys
from StringIO import StringIO
from unittest import TestCase

from tennis_calculator_app import main


class TennisCalculator(TestCase):

    def setUp(self):
        self.stdin = sys.stdin
        self.stdout = sys.stdout

    def tearDown(self):
        sys.stdin = self.stdin
        sys.stdout = self.stdout

    def test_integration(self):
        main(['test_data/simple_game.txt'])

        sys.stdin = StringIO("Games Player Person A")

        expout = """Incomplete game: p1 vs p2
        0 sets to 0
        1 0"""
        self.assertEqual(expout, sys.stdout.getvalue)

        sys.stdin = StringIO("Score Match 01")

        expout = """Incomplete game: p1 vs p2
0 sets to 0
1 0"""
        self.assertEqual(expout, sys.stdout.getvalue)

