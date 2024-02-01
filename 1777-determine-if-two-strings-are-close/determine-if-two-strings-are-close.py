class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False

        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for c1, c2 in zip(word1, word2):
            d1[c1] += 1
            d2[c2] += 1
            
        #the keys should be the same since we sorted the strings
        #the sorted values should match the keys of both strings
        return d1.keys() == d2.keys() and sorted(d1.values()) == sorted(d2.values())