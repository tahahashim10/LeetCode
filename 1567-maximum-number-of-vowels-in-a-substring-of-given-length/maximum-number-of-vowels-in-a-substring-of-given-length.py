class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        curr_subarray = s[:k].count('a') + s[:k].count('e') + s[:k].count('i') + s[:k].count('o') + s[:k].count('u')
        result = [curr_subarray]

        for i in range(1, len(s) - k + 1):
            curr_subarray -= (1 if s[i-1] in vowels else 0)
            curr_subarray += (1 if s[i+k-1] in vowels else 0)

            result.append(curr_subarray)
        
        return max(result)

