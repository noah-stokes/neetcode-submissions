class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (target - position) // speed = hours
        # 3, 2, 1, 4, 5, 2
        # if a car < a car in front of it, it will finish with that car
        # else it will finish after
        cars = sorted(zip(position, speed))

        if len(position) == 1:
            return 1

        res = 1
        stack = []
        for p, s in cars:
            stack.append((target - p) / s)
        
        prev = stack.pop()

        while stack:
            curr = stack.pop()

            if curr > prev:
                res += 1
                prev = curr

        return res



            
