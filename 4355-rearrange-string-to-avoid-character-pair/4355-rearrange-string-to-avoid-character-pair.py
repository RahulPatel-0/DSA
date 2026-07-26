class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        xc=[]
        oc=[]
        yc=[]
        for c in s:
            if c==x:
                xc.append(c)
            elif c==y:
                yc.append(c)
            else:
                oc.append(c)
        return "".join(yc+oc+xc)
        