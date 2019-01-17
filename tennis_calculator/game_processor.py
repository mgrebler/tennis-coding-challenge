from collections import namedtuple

GameResult = namedtuple('GameResult', ['winner', 'person_0_score', 'person_1_score'])

def process_game(points):
    p0 = 0
    p1 = 0

    while points:
        p = points.pop(0)
        if p == 0:
            p0 += 1
        elif p == 1:
            p1 += 1
        else:
            raise ValueError("Points must be 1 or 0")

        if abs(p0 - p1) > 1:
            if p0 > 3:
                return GameResult(0, p0, p1), points

            if p1 > 3:
                return GameResult(1, p0, p1), points
