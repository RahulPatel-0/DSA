class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n-1):
            curr,next=nums[i],nums[i+1]
            if next-curr>1:
                for j in range(curr+1,next):
                    res.append(j)
        return res
        