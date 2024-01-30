class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # solution 1
        # d = {}
        # # populating dictionary with all the values
        # for i in range(len(arr)):
        #     if arr[i] in d:
        #         d[arr[i]] += 1
        #     else:
        #         d[arr[i]] = 1

        # # converting the values to a set ensures that s has only the unique values
        # s = set(d.values())
        # print(s)


        # #d has all the values while s has only the unique values
        # return len(s) == len(d)

        #solution 2 (optimized)

        # c is dictionary-like and has all the values
        c = Counter(arr)
        
        #using a set ensures we have only the unique values
        unique_values = set(c.values())

        return len(unique_values) == len(c)