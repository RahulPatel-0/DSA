from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd=[]
        maxi=float('-inf')
        for num in nums:
            maxi=max(num,maxi)
            prefixGcd.append(gcd(num,maxi))
        prefixGcd.sort()
        n=len(prefixGcd)
        i,j=0,n-1
        ans=0
        while i<j:
            ans+=gcd(prefixGcd[i],prefixGcd[j])
            i+=1
            j-=1
        return ans



        