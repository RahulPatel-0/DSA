class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        miniindex=nums.index(min(nums))
        maxiindex=nums.index(max(nums))
        l=min(miniindex,maxiindex)
        r=max(miniindex,maxiindex)
        n=len(nums)
        if(n==1):
            return 1
        return min(r+1,n-l,l+1+n-r)