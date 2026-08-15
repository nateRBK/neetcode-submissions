class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        s = ''.join(c for c in s if c.isalnum())
        L,R = 0, len(s)-1
        while L < R:
            if s[L] != s[R]:
                return False
            else:
                L += 1
                R -= 1
        return True