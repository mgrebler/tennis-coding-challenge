def query_match(match_id, results):
    match = results.get(match_id)

    if not match:
        raise ValueError("Match '%s' not found." % match_id)

    return _print_match(match)


def _print_match(match):
    match_result = match.match_result
    print match_result
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

    result = "%s sets to %s\n" % sets_summary_counts
    result += _print_set_results(winner, match_result.set_results)
    return result


def _print_set_results(winner, set_results):
    result = ""
    for set in set_results:
        set_scores = (set.person_0_games, set.person_1_games)
        if winner == 1:
            set_scores = (set.person_1_games, set.person_0_games)

        result += "%s %s\n" % set_scores
    return result
