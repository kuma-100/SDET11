from unit.div import div


def test_div_int():
    assert div(10, 2) == 5
    assert div(1, 1) == 1


def test_div_float():
    assert div(10 / 3) == 3.33
    assert div(5.0 / 2.0) == 2.5


def test_div_expection():
    assert div(10, 'a')
    assert div('abc', 10)


def test_div_zero():
    assert div(10, 0) == None
