class Solution:
    def removeStars(self, s: str) -> str:
        s1 = []
        for i in s:
            if i == "*":
                s1.pop()
            else:
                s1.append(i)
        return ''.join(s1)

