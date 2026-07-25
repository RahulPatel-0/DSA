class Solution:
    def maxProduct(self, n: int) -> int:
        first=second=0
        while n>0:
            rem=n%10
            if rem>first:
                first,second=rem,first
            elif rem>second:
                second=rem
            n//=10
        return first*second
        