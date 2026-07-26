class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if(n==1):
            return s
        elif n==2:
            return s+m
        
        ans=(s+m)+(n//2-1)*(m-1)
        return ans
        