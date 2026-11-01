class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        ans=float('inf')
        for i in range(0,len(nums)-1,2):
            curr=int(str(nums[i])+str(nums[i+1]))
            if curr<ans:
                ans=curr
        return ans
        