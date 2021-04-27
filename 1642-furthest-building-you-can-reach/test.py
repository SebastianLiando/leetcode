from main import Solution

def calculate_result(heights, bricks, ladders):
    sol = Solution()
    return sol.furthestBuilding(heights, bricks, ladders)

def test_case_1():
    assert calculate_result([4,2,7,6,9,14,12], 5, 1) == 4

def test_case_2():
    assert calculate_result([4,12,2,7,3,18,20,3,19], 10, 2) == 7

def test_case_3():
    assert calculate_result([14, 3, 19, 3], 17, 0)

def test_case_edge_1():
    assert calculate_result([1, 14], 0, 0) == 0

def test_case_edge_2():
    assert calculate_result([1, 14], 5, 0) == 0

def test_case_edge_3():
    assert calculate_result([1, 14], 0, 1) == 1