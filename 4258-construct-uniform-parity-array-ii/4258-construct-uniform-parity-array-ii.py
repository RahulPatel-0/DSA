class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        smallestElement=min(nums1)
        #smallest is odd we can convert all the element to odd
        if smallestElement%2==1:
            return True
        for i in nums1:
            if i%2==1:
                return False
        return True
        