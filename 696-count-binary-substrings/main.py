class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Declare the counts
        counts = {'1': 0, '0': 0}
        
        # Saves the previous character
        prev_char = ''

        # Declare the result variable
        result = 0

        # Iterate through the string
        for char in s:
            # If changed, reset the count for that character
            if prev_char != char:
                counts[char] = 1
            else:
                counts[char] += 1
            
            if char == '0' and counts['1'] >= 1:
                counts['1'] -= 1
                result += 1
            
            if char == '1' and counts['0'] >= 1:
                counts['0'] -= 1
                result += 1
            
            # Update previous character
            prev_char = char

        return result
