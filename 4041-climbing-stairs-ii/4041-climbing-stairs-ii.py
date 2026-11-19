class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        #Recurrsion Approach
        # def solve(i,n,costs):
        #     if(i==n):
        #         return 0
        #     ans=float('inf')
        #     j=i+1
        #     if(j<=n):
        #         cost=costs[j-1]+(j-i)**2+solve(j,n,costs)
        #         ans=min(ans,cost)

        #     j=i+2
        #     if(j<=n):
        #         cost=costs[j-1]+(j-i)**2+solve(j,n,costs)
        #         ans=min(ans,cost)
            
        #     j=i+3
        #     if(j<=n):
        #         cost=costs[j-1]+(j-i)**2+solve(j,n,costs)
        #         ans=min(ans,cost)
        #     return ans
        # return solve(0,n,costs)

        #Dp Approach
        dp=[-1]*(n+1)
        def solve(i,n,costs):
            if(i==n):
                return 0
            if dp[i]!=-1:
                return dp[i]
            ans=float('inf')
            j=i+1
            if(j<=n):
                cost=costs[j-1]+(j-i)**2+solve(j,n,costs)
                ans=min(ans,cost)

            j=i+2
            if(j<=n):
                cost=costs[j-1]+(j-i)**2+solve(j,n,costs)
                ans=min(ans,cost)
            
            j=i+3
            if(j<=n):
                cost=costs[j-1]+(j-i)**2+solve(j,n,costs)
                ans=min(ans,cost)
            dp[i]= ans
            return dp[i]
        
        return solve(0,n,costs)
            
        