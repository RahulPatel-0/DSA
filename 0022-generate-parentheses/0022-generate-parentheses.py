class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtracking(openCount,closeCount,current,res):
            if openCount==n and closeCount==n:
                res.append(current)
                return 
            if openCount<n:
                backtracking(openCount+1,closeCount,current+'(',res)
            if closeCount<openCount:
                backtracking(openCount,closeCount+1,current+')',res)
        res=[]
        backtracking(0,0,"",res)
        return res
        