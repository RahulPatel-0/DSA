class Solution:
    def smallestPalindrome(self, s: str) -> str:
        mid=len(s)//2
        start=sorted(s[:mid])
        if len(s)%2==1:
            midElement=[s[mid]]
        else:
            midElement=[]
        reversedElement=start[::-1]
        return "".join(start+midElement+reversedElement)
        