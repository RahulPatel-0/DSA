class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        left=0
        count=0
        for i in range(len(nums)):
            if(nums[i]<minK or nums[i]>maxK):
                left=i+1
            else:
                count+=i-left+1
        return count
        