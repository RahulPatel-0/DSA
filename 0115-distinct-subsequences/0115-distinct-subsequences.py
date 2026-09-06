class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def Solve(s,t,i,j,dp):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if(s[i]!=t[j]):
                ans= Solve(s,t,i+1,j,dp)
                dp[i][j]=ans
                return  ans
            else:
                ans= Solve(s,t,i+1,j,dp)+Solve(s,t,i+1,j+1,dp)
                dp[i][j]=ans
                return ans
        m=len(s)
        n=len(t)
        dp=[[-1]*n for i in range(m)]
        return Solve(s,t,0,0,dp)
        