from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # Count the number of errors
        err = 0
        err_index = []

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                err += 1
                err_index.append(i)
        
        # Already ascending
        if err == 0:
            return True

        # More than 1 descending is impossible to fix
        if err > 1:
            return False

        # Check if the error can be fixed - not in the YABY scenario
        y1 = err_index[0] - 1
        y2 = err_index[0] + 2

        return not (
            y1 >= 0 and 
            y1 < len(nums) and 
            y2 < len(nums) and
            nums[y1] > nums[y1 + 2] and
            nums[y2] < nums[y1 + 1] 
        )

def calculate(nums):
    return Solution().checkPossibility(nums)

def test_case_one():
    assert calculate([4, 2, 3])

def test_case_two():
    assert not calculate([4, 2, 1])

def test_case_three():
    assert not calculate([3, 4, 2, 3])

def test_case_four():
    assert calculate([5, 7, 1, 8])

def test_case_sorted():
    assert calculate([1, 2, 3, 4])

def test_case_equal():
    assert calculate([7, 5, 5, 5])

def test_case_equal_two():
    assert calculate([5, 7, 5, 5])

def test_case_one_element():
    assert calculate([2])