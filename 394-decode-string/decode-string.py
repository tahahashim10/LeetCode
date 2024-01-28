class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]": # we dont reach a subproblem until we find a closed bracket
                stack.append(c)
            else:
                substring = ""

                while stack[-1] != "[": # now we will reverse from the "]" to the "[" to get the substring
                    substring = stack.pop() + substring # dont want a reversed string, dont do substring += stack.pop()

                stack.pop() # pop the "[" dont need it

                k = ""

                while stack and stack[-1].isdigit():                
                    k = stack.pop() + k # dont want a reversed string, dont do k += stack.pop()
                
                stack.append(int(k) * substring)
        
        return ''.join(stack)
                
            
        