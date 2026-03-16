from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


# --- Bug: check_guess hint messages were inverted ---
# "Too High" showed "Go HIGHER!" and "Too Low" showed "Go LOWER!"

def test_too_high_hint_says_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_hint_says_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- Bug: get_range_for_difficulty had Normal and Hard ranges inverted ---
# Normal was returning 1-100, Hard was returning 1-50

def test_normal_difficulty_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 50

def test_hard_difficulty_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 100


# --- Bug: update_score applied attempt_number + 1, double-counting the increment ---
# Win on attempt 1 gave 80 points instead of 90

def test_win_score_attempt_1():
    score = update_score(0, "Win", 1)
    assert score == 90  # 100 - 10 * 1

def test_win_score_attempt_5():
    score = update_score(0, "Win", 5)
    assert score == 50  # 100 - 10 * 5

def test_win_score_floor_at_10():
    score = update_score(0, "Win", 10)
    assert score == 10  # would be 0, floored to 10


# --- Bug: update_score gave +5 on even Too High attempts and -5 on odd ---
# Score should never change on a wrong guess

def test_too_high_even_attempt_no_score_change():
    score = update_score(50, "Too High", 2)
    assert score == 50

def test_too_high_odd_attempt_no_score_change():
    score = update_score(50, "Too High", 3)
    assert score == 50

def test_too_low_no_score_change():
    score = update_score(50, "Too Low", 1)
    assert score == 50


# --- Bug: parse_guess did not validate against difficulty range ---
# A guess outside the range was accepted as valid

def test_guess_above_range_rejected():
    ok, value, err = parse_guess("25", 1, 20)
    assert ok == False
    assert value is None

def test_guess_below_range_rejected():
    ok, value, err = parse_guess("0", 1, 20)
    assert ok == False
    assert value is None

def test_guess_within_range_accepted():
    ok, value, err = parse_guess("10", 1, 20)
    assert ok == True
    assert value == 10


# --- Bug: invalid guess (non-numeric) was consuming an attempt ---
# parse_guess should return ok=False so attempts are not incremented

def test_non_numeric_input_not_ok():
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok == False
    assert value is None

def test_empty_input_not_ok():
    ok, value, err = parse_guess("", 1, 100)
    assert ok == False
    assert value is None
