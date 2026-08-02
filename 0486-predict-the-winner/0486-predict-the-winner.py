class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(i,j):
            if i>j:
                return 0
            if i==j:
                return nums[i]
            take_i=nums[i]+min(solve(i+1,j-1),solve(i+2,j))
            take_j=nums[j]+min(solve(i+1,j-1),solve(i,j-2))
            return max(take_i,take_j)
        n=len(nums)
        p1=solve(0,n-1)
        p2=sum(nums)-p1
        return not p2>p1

        