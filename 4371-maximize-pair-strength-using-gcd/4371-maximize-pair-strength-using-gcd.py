import math
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        maxi=-1
        n=len(nums)
        for i in range(1,n):
            for j in range(i):
                n=nums[i]*nums[j]
                gcd=math.gcd(nums[i],nums[j])
                maxi=max(maxi,n//(gcd*gcd))
   
        return maxi

        