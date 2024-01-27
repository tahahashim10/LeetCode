class RecentCounter:

    def __init__(self):
        self.requests = []
        

    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        # keep removing elements that arent in the range
        # since t is increasing, left get larger so if requests[0] < left bound of t, then itll be less than left bound at a greater t too
        # if requests[0] > right bound then it might still be > larger right bound
        leftbound = t - 3000
        while self.requests and (leftbound > self.requests[0] ): 
            self.requests.pop(0) # not in between bounds

        return len(self.requests)