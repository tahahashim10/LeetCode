class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for a in asteroids:
            # we only have a collision when a < 0 and stack[-1] > 0
            while stack and a < 0 < stack[-1]:
                if abs(a) > abs(stack[-1]): # stack[-1] destroyed
                    stack.pop()
                elif abs(a) < abs(stack[-1]): #a destroyed
                    a = 0 #asteroids[i] != 0 so we cant add 0 to stack and loop stops
                else: # a and stack[-1] destroyed
                    stack.pop()
                    a = 0
            #no collision so we append a
            if a != 0:
                stack.append(a)
        
        return stack