class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curMax = -1
        ans = [0]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            ans[i] = curMax
            curMax = max(arr[i], curMax)

        return ans