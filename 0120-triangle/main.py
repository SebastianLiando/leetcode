from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                top_center = 10001 if j >= len(triangle[i-1]) else triangle[i-1][j]
                top_left = 10001 if j-1 < 0 else triangle[i-1][j-1]
                top_right = 10001 if j+1 >= len(triangle[j]) else triangle[i-1][j+1] 
                
                triangle[i][j] = min(top_center, top_left, top_right) + triangle[i][j]

        return min(triangle[-1])