from collections import namedtuple

MatchResult = namedtuple('MatchResult', ['winner', 'person_0_sets', 'person_1_sets'])

class MatchProcessor:
    max_sets = 0

    def __init__(self, max_sets):
        self.max_sets = max_sets

    def process_match(self, points):
        remaining_points = points

        s0 = 0
        s1 = 0

