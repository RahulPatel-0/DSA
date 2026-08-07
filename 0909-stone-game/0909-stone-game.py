class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[[-1]*n for _ in range(n)]
        def AliceScore(i,j):
            if i>j:
                return 0
            if i==j:
                return nums[i]
            if dp[i][j]!=-1:
                return dp[i][j]
            take_i=nums[i]+min(AliceScore(i+2,j),AliceScore(i+1,j-1))
            take_j=nums[j]+min(AliceScore(i,j-2),AliceScore(i+1,j-1))
            dp[i][j]=max(take_i,take_j)
            return dp[i][j]
        
        alice=AliceScore(0,n-1)
        bob=sum(nums)-alice
        return alice>bob
        