class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        j = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        temp = []
        length = len(s)
        for i in range(length):
            if s[i] in vowels:
                temp.append(s[i])
                j += 1
        for i in range(length):
            if s[i] in vowels:   
                j -= 1         
                s[i] = temp[j]
        return ''.join(s)

        


        