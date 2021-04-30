from typing import List

class Solution:
    def __init__(self):
        self.cache = {}

    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Base case - target is 0, add as solution
        if target == 0:
            print("found")
            return 1

        # Base case - solution has been computed before
        if target in self.cache.keys():
            print("cache hit")
            return self.cache[target]

        ans = 0

        # Iterate the list
        for num in nums:
            # If the element is <= target, add as potential solution
            if num <= target:
                ans += self.combinationSum4(nums, target - num)

        # Memoize and return
        self.cache[target] = ans
        return ans

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