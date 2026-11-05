class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums)
        target_index=n//2
        count=0
        nums.sort()
        # Approach 1
        # for i in range(n):
        #     count+=abs(nums[i]-nums[target_index])
        # return count
        
        # Approach 2
        for i in range(n//2):
            count+=abs(nums[i]-nums[target_index])
            count+=abs(nums[n-i-1]-nums[target_index])
        return count
