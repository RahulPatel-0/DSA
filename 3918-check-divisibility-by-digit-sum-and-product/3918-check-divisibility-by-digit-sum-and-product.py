class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s1=n
        p=1
        s=0
        print("s",s)
        while s1>0:
            r=s1%10
            p*=r
            s+=r
            s1=s1//10
        print(p,s)
        return n%(p+s)==0
        