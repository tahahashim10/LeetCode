class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        s1 = ""
        length = len(s)
        for i in range(length):
            s1 += s[i] + " "
        return s1[:len(s1) - 1]
        