from judge_code import game_over

def test_game_over_0():
    assert game_over(0) is True

def test_game_over_666():
    assert game_over(666) is False

def test_game_over_other():
    assert game_over(333) is False
