class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        curr_subarray = sum(1 for char in s[:k] if char in vowels)
        result = curr_subarray

        for i in range(1, len(s) - k + 1):
            curr_subarray -= (1 if s[i-1] in vowels else 0)
            curr_subarray += (1 if s[i+k-1] in vowels else 0)

            result = max(result, curr_subarray)
        
        return result

