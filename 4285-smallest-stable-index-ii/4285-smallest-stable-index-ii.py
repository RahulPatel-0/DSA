class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        minFromIndex=[10**9+1]*n
        minElement=nums[-1]
        minFromIndex[n-1]=minElement
        for i in range(n-2,-1,-1):
            minElement=min(nums[i],minElement)
            minFromIndex[i]=minElement
        maxElement=float('-inf')
        for i in range(n):
            maxElement=max(maxElement,nums[i])
            if maxElement-minFromIndex[i]<=k:
                return i
        return -1

        
        