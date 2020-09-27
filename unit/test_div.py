import pytest

from unit.div import div


@pytest.mark.happy
def test_div_int():
    assert div(10, 2) == 5
    assert div(10, 5) == 4
    assert div(1, 1) == 1


@pytest.mark.happy
@pytest.mark.parametrize("number1,number2,expection", {
    (10, 2, 5),
    (1, 1, 1),
    (10, 5, 4),
    (100000, 1, 100000),
    (100, 200, 0.5)
})
def test_div_int_param(number1, number2, expection):
    assert div(number1, number2) == expection


@pytest.mark.happy
def test_div_float():
    assert div(10 / 3) == 3.33
    assert div(5.0 / 2.0) == 2.5


@pytest.mark.expection
def test_div_expection():
    assert div(10, 'a')
    assert div('abc', 10)


@pytest.mark.expection
def test_div_zero():
    assert div(10, 0) == None


@pytest.mark.expection
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
