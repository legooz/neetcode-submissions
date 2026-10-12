class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        consecutive_ones = 0
        longest_consecutive_ones = 0

        for num in nums:
            if num == 1:
                consecutive_ones += 1
            elif num == 0:
                consecutive_ones = 0
            
            if consecutive_ones > longest_consecutive_ones:
                longest_consecutive_ones = consecutive_ones
        
        return longest_consecutive_ones