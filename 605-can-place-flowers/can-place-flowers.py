class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0 or (flowerbed == [0] and n == 1):
            return True
        n1 = 0
        length = len(flowerbed) - 1
        length2 = len(flowerbed) - 2
        for i in range(length):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n1 += 1
            elif i == length2 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n1 += 1
            elif flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n1 += 1
        if n <= n1: 
            return True
        return False

        