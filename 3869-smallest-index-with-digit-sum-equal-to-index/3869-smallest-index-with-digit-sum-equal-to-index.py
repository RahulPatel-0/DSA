class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitSum(s):
            total=0
            while s:
                num,digit=divmod(s,10)
                total+=digit
                s=s//10
            return total
        for i ,num in enumerate(nums):
            if digitSum(num)==i:
                return i
        return -1
                
            


        