from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1

        result_start = -1
        result_end = -1

        while start <= end:
            center = (end + start) // 2

            if nums[center] == target and (center == 0 or nums[center - 1] < target):
                result_start = center
                break
            
            # If center value is less than the target, search the right
            elif nums[center] < target:
                start = center + 1

            # If center value is more than the target, search the left
            # If the target value is not the first occurrence, go left
            else:
                end = center - 1

        start = 0
        end = len(nums) - 1        

        while start <= end:
            center = (end + start) // 2

            if nums[center] == target and (center == len(nums) - 1 or nums[center + 1] > target):
                result_end = center
                break
            
            # If center value is more than the target, search the left
            elif nums[center] > target:
                end = center - 1

            # If center value is less than the target, search the right
            # If the target value is not the first occurrence, go right
            else:
                start = center + 1

        return [result_start, result_end]

def calculate(list_in, target):
    return Solution().searchRange(list_in, target)

def test_case_1():
    assert calculate([5,7,7,8,8,10], 8) == [3, 4]

def test_case_2():
    assert calculate([1,1,1,2,2,2], 2) == [3, 5]

def test_case_not_found():
    assert calculate([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

def test_case_empty():
    assert calculate([], 2) == [-1, -1]