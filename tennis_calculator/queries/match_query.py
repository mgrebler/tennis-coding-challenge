import re


def get_match_id(query_string):
    m = re.match("Score Match (?P<match_id>.*$)", query_string)
    if m:
        return m.group('match_id')


def query_match(match_id, results):
    match = results.get(match_id)

    if not match:
        raise ValueError("Match '%s' not found." % match_id)

    return _print_match(match)


def _print_match(match):
    match_result = match.match_result
    winner = match_result.winner

    player_names = (match.person_0_name, match.person_1_name)

    if winner is None:
        result = "Incomplete game: %s vs %s\n" % player_names
        winner = 0
    else:
        if winner == 1:
            player_names = (match.person_1_name, match.person_0_name)
        result = "%s defeated %s\n" % player_names

    result += _print_match_results(winner, match_result)
    return result


def _print_match_results(winner, match_result):
    sets_summary_counts = (match_result.person_0_sets, match_result.person_1_sets)
    if winner == 1:
        sets_summary_counts = (match_result.person_1_sets, match_result.person_0_sets)

    return "%s sets to %s\n" % sets_summary_counts

