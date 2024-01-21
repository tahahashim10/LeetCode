class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # check if there even is a gcd, if there isnt return empty string
        if str1 + str2 != str2 + str1:
            return ""
        else:
            return str1[0: gcd(len(str1), len(str2))]
                
        
"
