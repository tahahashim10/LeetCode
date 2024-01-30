class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
    
        unique_values = set(c.values())

        return len(unique_values) == len(c)