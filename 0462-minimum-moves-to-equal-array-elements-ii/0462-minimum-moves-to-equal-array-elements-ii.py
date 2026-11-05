class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums)
        target_index=n//2
        count=0
        nums.sort()
        for i in range(n):
            count+=abs(nums[i]-nums[target_index])
        return count
        