class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        result = []
        hold = {}

        for word in strs:
            wordSorted = ''.join(sorted(word))
            if wordSorted not in hold:
                hold[wordSorted] = [word]
            else:
                hold[wordSorted].append(word)
        for item in hold:
            result.append(hold[item])
        return result