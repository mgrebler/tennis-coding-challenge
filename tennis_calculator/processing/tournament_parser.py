from tennis_calculator.processing import match_processor
from tennis_calculator.results.results import NamedMatchResult


def parse_tournament(score_file):
    r, m, p0, p1, p = {}, None, None, None, [] # results, match, points, player 0, player 1

    for l in score_file:
        l_ = l.strip()

        lt = get_line_type(l_, m, p0)

        if lt == "1st match line":
            # check for the first match line.
            if l_.find("Match: ") == 0:
                m = l_[7:]
            else:
                # Raise value error if we don't find a match id
                raise ValueError("Expected Match but found line: %s" % l_)
        elif lt == "player line":
            # Check for player vs player line
            i = l_.find(" vs ")
            if i > -1:
                p0 = l_[:i]
                p1 = l_[(i + 4):]
            else:
                # Raise value error if don't match player
                raise ValueError("Expected player names but found line: %s" % l_)
        elif lt == "player 0 point":
            p.append(0)
        elif lt == "player 1 point":
            p.append(int(l_))
        elif lt == "blank line":
            # Ignore blank lines
            continue
        elif lt == "match line":
            r[m] = NamedMatchResult(m, p0, p1, match_processor.process_womens_match(p))
            # Check for player vs player line
            if l_.find("Match: ") == 0:
                m = l_[len("Match: "):]
            else:
                # Raise value error if don't match player
                raise ValueError("Expected Match but found line: %s" % l_)

            p0, p1 = None, None

            p = []

    r[m] = NamedMatchResult(m, p0, p1, match_processor.process_womens_match(p))

    return r


def get_line_type(l_, m, p0):
    if not m:
        lt = "1st match line"
    elif not p0:
        lt = "player line"
    elif l_ == "0":
        lt = "player 0 point"
    elif l_ == "1":
        lt = "player 1 point"
    elif not l_:
        lt = "blank line"
    else:
        lt = "match line"
    return lt

