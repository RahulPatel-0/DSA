class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ans=nums[0]
        for j in range(1,len(nums)):
            if nums[j]!=nums[j-1]+1:
                break
            ans+=nums[j]
        num_Set=set(nums)
        while ans in num_Set:
            ans+=1
        return ans
        