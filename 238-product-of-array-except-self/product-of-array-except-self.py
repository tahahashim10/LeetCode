class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        #calculate products of all numbers left to element i
        #start at index 1 since nothing to the left of index 0 
        
        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i-1]

        #calculate products of all numbers to the right of element i
        right = nums[-1]
        # nothing to the right of last index so dont start there
        for i in range(length - 2, -1, -1):
            answer[i] *= right
            right *= nums[i]
        return answer
