class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor=0
        n=len(nums)
        allZero=True
        for i in nums:
            xor^=i
            if i !=0:
                allZero=False
        if allZero:
            return 0
        if xor==0:
            return n-1
        return n
        