class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        target = len(nums)//2
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1 
        for el in d: 
            if d[el] > target:
                return el
        return -1