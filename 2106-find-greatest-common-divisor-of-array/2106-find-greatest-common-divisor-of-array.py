class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini=min(nums)
        maxi=max(nums)
        ans=1
        for i in range(2,min(maxi,mini)+1):
            if mini%i==0 and maxi%i==0:
                ans=i
        return ans