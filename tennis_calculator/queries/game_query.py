def query_games(player_name, results):
    games_for = 0
    games_against = 0

    for _, named_match_result in results.iteritems():

        match_result = named_match_result.match_result

        if not _is_player_in_match(named_match_result, player_name):
            continue

        a, b = _get_games_from_set(match_result.set_results)
        if named_match_result.person_1_name == player_name:
            a, b = b, a

        games_for += a
        games_against += b

    return "%s %s" % (games_for, games_against)


def _is_player_in_match(match_result, player_name):
    return match_result.person_0_name == player_name or match_result.person_1_name == player_name


def _get_games_from_set(set_results):
    a, b = 0, 0
    for set in set_results:
        a += set.person_0_games
        b += set.person_1_games

    return a, b

