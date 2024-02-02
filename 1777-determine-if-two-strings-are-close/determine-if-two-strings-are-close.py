class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False

        # d1 = defaultdict(int)
        # d2 = defaultdict(int)

        # for c1 in word1:
        #     d1[c1] += 1
        # for c2 in word2:
        #     d2[c2] += 1

        d1 = [0] * 26
        d2 = [0] * 26

        for c1 in word1:
            d1[ord(c1) - ord('a')] += 1
        for c2 in word2:
            d2[ord(c2) - ord('a')] += 1

        return sorted(d1) == sorted(d2) and set(word1) == set(word2)

        
            
        #the keys should be the same since we sorted the strings
        #the sorted values should match the keys of both strings
        # return d1.keys() == d2.keys() and sorted(d1.values()) == sorted(d2.values())
        