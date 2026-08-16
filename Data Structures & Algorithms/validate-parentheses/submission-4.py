class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        d = {')':'(',
             '}':'{',
             ']':'['}
        for c in s:
            if c not in ')]}':
                stack.append(c)
            elif not stack or d[c] != stack.pop():
                return False
        return not stack