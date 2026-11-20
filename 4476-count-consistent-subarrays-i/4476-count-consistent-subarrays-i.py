class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            add_val=nums[i]
            min_val=nums[i]
            for j in range(i,n):
                add_val &=nums[j]
                if nums[j]<min_val:
                    min_val=nums[j]
                if add_val==min_val:
                    count+=1
        return count

        