class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n-1):
            if nums[i+1] ^ nums[i]==0:
                count+=1
        return count
        