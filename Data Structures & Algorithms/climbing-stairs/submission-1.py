from functools import cache

@cache
def staircase(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
        

    return staircase(n - 2) + staircase(n - 1)

    


class Solution:
    def climbStairs(self, n: int) -> int:


        count = staircase(n)

        return count