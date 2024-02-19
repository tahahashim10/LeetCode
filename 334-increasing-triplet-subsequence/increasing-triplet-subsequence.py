class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstTriplet = secondTriplet = float('inf')
        length = len(nums)
        for i in range(length):
            if nums[i] <= firstTriplet:
                firstTriplet = nums[i]
            elif nums[i] <= secondTriplet:
                secondTriplet = nums[i]
            elif nums[i] > secondTriplet:
                return True
        return False

#first = 0
#second = 4
#third = 6