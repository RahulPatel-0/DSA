class Solution:
    def countCommas(self, n: int) -> int:
        # lower=1000
        # comma=1
        # result=0
        # while lower<=n:
        #     upper=lower*1000-1
        #     if(upper>n):
        #         upper=n
        #     countOfNo=upper-lower+1
        #     result+=countOfNo*comma
        #     comma+=1
        #     lower*=1000
        # return result
        #Approach 2
        start=1000
        result=0
        while start<=n:
            result+=n-start+1
            start*=10**3
        return result
        