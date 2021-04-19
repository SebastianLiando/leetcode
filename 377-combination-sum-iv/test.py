from main import Solution

def calculate_solution(list_in, target) -> int:
    sol = Solution()
    return sol.combinationSum4(list_in, target)

def test_case_1():
    assert calculate_solution([1, 2, 3], 4) == 7

def test_case_empty():
    assert calculate_solution([], 3) == 0

def test_case_all_ones():
    assert calculate_solution([1], 5) == 1

def test_case_2():
    assert calculate_solution([1, 2, 3], 3) == 4