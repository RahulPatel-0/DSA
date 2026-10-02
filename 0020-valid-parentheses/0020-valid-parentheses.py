class Solution:
    def isValid(self, s: str) -> bool:
        l=['(','{','[']
        stack=[]
        for char in s:
            if char in l:
                stack.append(char)
            else:
                if not stack:
                    return False
                current=stack.pop()
                if current=='(':
                    if char!=')':
                        return False
                if current=='{':
                    if char!='}':
                        return False
                if current=='[':
                    if char!=']':
                        return False
        if stack:
            return False
        return True

                    