class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        #Approach 1
        # evenSum=n*n+n
        # oddSum=n*n
        # x=min(evenSum,oddSum)+1
        # ans=1
        # for i in range(2,x+1):
        #     if evenSum%i==0 and oddSum%i==0:
        #         ans=i
        # return ans

        #Approach 2
        #Key observation
        # oddSum=n*n
        # evenSum=n*(n+1)=n*n+n
        # gcd(n*n,n*(n+1))=n
        return n

        