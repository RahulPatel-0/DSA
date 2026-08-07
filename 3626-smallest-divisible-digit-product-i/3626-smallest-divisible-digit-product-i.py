class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def ProductDigit(n):
            prod=1
            while n>0:
                rem=n%10
                prod*=rem
                n//=10
            return prod
        
        for i in range(n,n+10):
            if(ProductDigit(i)%t==0):
                return i

        