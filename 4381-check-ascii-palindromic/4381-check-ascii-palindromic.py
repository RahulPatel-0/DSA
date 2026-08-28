class Solution:
    def isPalindromic(self, s: str) -> bool:
        ans=""
        for i in s:
            ans+=format(ord(i),'08b')
        return ans==ans[::-1]
        