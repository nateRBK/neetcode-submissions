class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            diff = ord(s[i+1]) - ord(s[i])
            if diff > 0:
                score += diff
            if diff < 0:
                score -= diff
        return score