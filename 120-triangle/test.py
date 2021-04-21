from main import Solution

def calculate_solution(triangle):
    solution = Solution()
    return solution.minimumTotal(triangle)

def test_case_1():
    assert calculate_solution([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11

def test_case_2():
    assert calculate_solution([[-10]]) == -10