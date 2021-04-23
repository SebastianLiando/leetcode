from main import Solution

def calculate_result(input_string):
    solution = Solution()
    return solution.countBinarySubstrings(input_string)

def test_case_1():
    assert calculate_result('00110011') == 6

def test_case_2():
    assert calculate_result('10101') == 4

def test_case_3():
    assert calculate_result('00100') == 2

def test_case_edge_1():
    assert calculate_result('1') == 0

def test_case_edge_2():
    assert calculate_result('0') == 0

def test_case_overlapping():
    assert calculate_result('0000111100') == 6

def test_case_long():
    assert calculate_result('000011110010') == 8