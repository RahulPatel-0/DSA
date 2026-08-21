class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        m=len(requests)
        ans=requests[0]
        
        for i in range(1,m):
            ans+=abs(requests[i]-requests[i-1])
        return ans

        