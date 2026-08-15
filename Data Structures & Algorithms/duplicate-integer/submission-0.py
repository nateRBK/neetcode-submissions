class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        
        tainer = set()
        for item in nums:
            if item in tainer:
                return True
            tainer.add(item)
        return False
