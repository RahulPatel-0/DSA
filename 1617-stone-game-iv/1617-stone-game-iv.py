from math import isqrt
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo={}
        def solve(n):
            if n==0:
                return False
            if n in memo:
                return memo[n]
            for k in range(1, isqrt(n) + 1):
                v=n-k**2
                if(solve(v)==False):
                    memo[n]=True
                    return True
            memo[n]=False
            return False
        return solve(n)
        