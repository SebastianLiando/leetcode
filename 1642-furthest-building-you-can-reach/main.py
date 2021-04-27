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