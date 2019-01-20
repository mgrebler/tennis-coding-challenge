from collections import namedtuple

GameResult = namedtuple('GameResult', ['winner', 'person_0_score', 'person_1_score'])
SetResult = namedtuple('SetResult', ['winner', 'person_0_games', 'person_1_games'])
MatchResult = namedtuple('MatchResult', ['winner', 'person_0_sets', 'person_1_sets'])
NamedMatchResult = namedtuple('NamedMatchResult', ['match_id', 'person_0_name', 'person_1_name', 'match_result'])

