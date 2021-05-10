import math


class Solution:
    def countPrimes(self, n: int) -> int:
        # Handle edge cases
        if n <= 1:
            return 0

        solutions = set([i for i in range(2, n)])

        terminate_num = int(math.sqrt(n))
        
        for i in range(2, terminate_num + 1):
            if i in solutions:
                for j in range(i * i, n, i):
                    if j in solutions:
                        solutions.remove(j)
        
        return len(solutions)

def calculate(n: int) -> int:
    return Solution().countPrimes(n)

def test_edge_one():
    assert calculate(1) == 0

def test_edge_zero():
    assert calculate(0) == 0

def test_case_one():
    assert calculate(10) == 4

def test_case_extreme():
    assert calculate(5 * 10 ** 6) > 1