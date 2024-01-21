class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x = []
        maxCandies = max(candies)
        length = len(candies)
        for i in range(length):
            if candies[i] + extraCandies < maxCandies:
                x.append(False)
            else:
                x.append(True)
        return x

        
[2,3,5,1,3]
