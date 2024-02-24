class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0

        start = 0
        end = 0
        flips_left = k

        #extend the sliding window until condition is met
        while end < len(nums):
            if nums[end] == 0:
                flips_left -= 1
            end += 1
            
            #contract sliding window until it doesnt meet condition
            while start < end and flips_left < 0:
                if nums[start] == 0:
                    flips_left += 1
                start += 1

            max_length = max(max_length, end-start)

        return max_length
