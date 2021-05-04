from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]

        for i in range(1, len(nums)):
            ans.append(ans[i - 1] + nums[i])
        
        return ans


def calculate(nums):
    return Solution().runningSum(nums)


def test_case_one():
    assert calculate([1,2,3,4]) == [1, 3, 6, 10]

def test_case_two():
    assert calculate([1, 1, 1, 1]) == [1, 2, 3, 4]

def test_case_three():
    assert calculate([3,1,2,10,1]) == [3,4,6,16,17]

def test_case_edge():
    assert calculate([1]) == [1]