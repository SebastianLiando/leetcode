from main import Solution

def calculate(n) -> bool:
    return Solution().isPowerOfThree(n)

def test_zero():
    assert not calculate(0)

def test_negative():
    assert not calculate(-102)

def test_positive():
    assert not calculate(15)

def test_power_of_threes():
    in_constraints = [3 ** i for i in range(20)]

    for n in in_constraints:
        assert calculate(n)