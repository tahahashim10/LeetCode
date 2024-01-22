class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n, radiants, dires = len(senate), [], []

        for i, c in enumerate(senate):
            radiants.append(i) if c == "R" else dires.append(i)
        
        while radiants and dires:
            r_i = radiants.pop(0)
            d_i = dires.pop(0)
            if d_i > r_i:
                radiants.append(r_i + n) # in case we loop
            else:
                dires.append(d_i + n) # in case we loop

        return "Radiant" if len(radiants) > len(dires) else "Dire"