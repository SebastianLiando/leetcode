class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 0 and negatives are false
        return n > 0 and 1162261467 % n == 0