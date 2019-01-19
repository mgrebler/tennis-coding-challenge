from collections import namedtuple

GameResult = namedtuple('GameResult', ['winner', 'person_0_score', 'person_1_score'])

NORMAL_GAME_POINTS = 4
TIE_BREAK_POINTS = 7

class GameProcessor:
    max_points = 0

    def __init__(self, max_points):
        self.max_points = max_points

    def process_game(self, points):
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
                if p0 >= self.max_points:
                    return GameResult(0, p0, p1), points

                if p1 >= self.max_points:
                    return GameResult(1, p0, p1), points

        return GameResult(None, p0, p1), points

def process_game(points):
    return process_game.game_processor.process_game(points)


process_game.game_processor = GameProcessor(NORMAL_GAME_POINTS)


def process_tiebreaker(points):
    return process_tiebreaker.game_processor.process_game(points)


process_tiebreaker.game_processor = GameProcessor(TIE_BREAK_POINTS)

