class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = {}

        for c in s:
            if c not in charCount:
                charCount[c] = 1
            else:
                charCount[c] += 1

        for c in t:
            if c not in charCount:
                return False
            else:
                if charCount[c] == 1:
                    charCount.pop(c)
                else:
                    charCount[c] -=1
        if len(charCount) != 0:
            return False
        else:
            return True
        