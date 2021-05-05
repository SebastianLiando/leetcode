from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize the variables
        steps = [10**6 for x in range(len(nums))]
        steps[0] = 0

        # Iterate on all element except the last one
        for i in range(len(nums) - 1):
            # Get the max step
            max_step = nums[i]
            
            # Get the minimal step to reach the current one
            min_step = steps[i]

            # Lookup the next n elements
            for j in range(i + 1, min(i + 1 + max_step, len(nums))):
                # Update only if the step is smaller
                steps[j] = min(steps[j], min_step + 1)

        # The solution is the last element of the step
        return steps[-1]
    

def calculate(nums: List[int]) -> int:
    return Solution().jump(nums)

def test_case_one():
    assert calculate([2,3,1,1,4]) == 2

def test_case_two():
    assert calculate([2,3,0,1,4]) == 2

def test_case_three():
    assert calculate([2, 2, 4, 3]) == 2

def test_case_one_element():
    assert calculate([1]) == 0

def test_case_thousand_elements():
    nums = [1 for x in range(1000)]
    assert calculate(nums) == 999
