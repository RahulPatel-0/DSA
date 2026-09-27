class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        if target==source:
            return 0
        sr,sc=source
        tr,tc=target
        rDiff=abs(sr-tr)
        cDiff=abs(sc-tc)
        if (rDiff==0 or cDiff==0 or cDiff==rDiff):
            return 1
        return 2

        