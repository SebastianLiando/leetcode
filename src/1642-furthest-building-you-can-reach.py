from typing import List
from heapq import heappop, heappush # O(log n) for push and pop

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heightsForLadders = []
        bricksRemaining = bricks
        laddersRemaining = ladders

        for i in range(len(heights) - 1):
            heightDiff = heights[i + 1] - heights[i]

            if heightDiff > 0 :
                # Exhaust the ladder in the beginning
                if laddersRemaining > 0:
                    heappush(heightsForLadders, heightDiff)
                    laddersRemaining -= 1
                else:
                    # If there is ladder
                    if ladders > 0:
                        # Compare with the smallest laddered
                        lowestLaddered = heightsForLadders[0]

                        if lowestLaddered < heightDiff:
                            heappop(heightsForLadders)
                            heappush(heightsForLadders, heightDiff)
                            bricksRemaining -= lowestLaddered
                        else:
                            bricksRemaining -= heightDiff
                            
                    # If there is no ladder at all
                    else:
                        bricksRemaining -= heightDiff

                    if bricksRemaining < 0:
                        return i
        
        return len(heights) - 1

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