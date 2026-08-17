class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        n = len(nums)
        for i in range(len(nums)):
            count = 0
            for j in range(i,n):
                if nums[j] == 0: break
                count += 1
            m = max(m, count)
        return m