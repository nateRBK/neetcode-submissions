class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curMax = -1
        n = len(arr)
        ans = [0]*n
        for i in range(n-1,-1,-1):
            ans[i] = curMax
            curMax = max(arr[i], curMax)

        return ans