import re

from tennis_calculator.processing import match_processor
from tennis_calculator.results.results import NamedMatchResult


def parse_tournament(score_file):
    results = {}

    match_id = None
    player_0 = None
    player_1 = None
    points = []

    for full_line in score_file:
        line = full_line.strip()
        if not line:
            continue
        if not match_id:
            match_id = _parse_match(line)
        elif not player_0:
            player_0, player_1 = _parse_players(line)
        elif line == "0" or line == "1":
            points.append(int(line))
        else:
            results[match_id] = _match_complete(match_id, player_0, player_1, points)
            match_id = _parse_match(line)
            player_0, player_1 = None, None
            points = []

    results[match_id] = _match_complete(match_id, player_0, player_1, points)

    return results


def _match_complete(match_id, player_0, player_1, points):
    match_result = match_processor.process_womens_match(points)
    return NamedMatchResult(match_id, player_0, player_1, match_result)


def _parse_match(line):
    m = re.match("Match: (?P<match_id>.*)", line)
    if m:
        match_id = m.group('match_id')
        if match_id:
            return match_id
    raise ValueError("Expected Match but found line: %s" % line)

def _parse_players(line):
    m = re.match("(?P<player_0>.*) vs (?P<player_1>.*)", line)
    if m:
        player_0 = m.group('player_0')
        player_1 = m.group('player_1')
        if player_0 and player_1:
            return player_0, player_1
    raise ValueError("Expected player names but found line: %s" % line)


