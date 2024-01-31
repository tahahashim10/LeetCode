class Solution:
    def removeStars(self, s: str) -> str:
        s1 = []

        for i in range(len(s)):
            if s[i] == "*" and len(s1) > 0:
                # if s1 and s1[-1] != "*":
                    s1.pop()
            else:
                s1.append(s[i])
            

        return ''.join(s1)

