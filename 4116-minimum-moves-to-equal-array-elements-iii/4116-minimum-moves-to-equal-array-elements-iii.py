class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi=max(nums)
        count=0
        for i in range(len(nums)):
            count+=abs(nums[i]-maxi)
        return count
        