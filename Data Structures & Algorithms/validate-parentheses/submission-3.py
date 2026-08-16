class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) == 0 and len(s) != 0: return False
                if stack[-1] != '(':
                    return False
                else:
                    stack.pop(-1)
            elif s[i] == '}':
                if len(stack) == 0 and len(s) != 0: return False
                if stack[-1] != '{':
                    return False
                else:
                    stack.pop(-1)
            elif s[i] == ']':
                if len(stack) == 0 and len(s) != 0: return False
                if stack[-1] != '[':
                    return False
                else:
                    stack.pop(-1)
        if len(stack) != 0:
            return False
        else:
            return True