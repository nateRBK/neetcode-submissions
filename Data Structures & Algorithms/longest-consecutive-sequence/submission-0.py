class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for item in nums:
            if (item-1) not in nums:
                length = 1
                while (item + length) in nums:
                    length += 1
                longest = max(length, longest)
        return longest
        
        #window of size 2, started at index 0
        #if items in window are consecutive, check if next item is consecutive
        #while true, increase window size, check again
        #once false, if no saved window, save window
        #else, if saved window, overwrite window
        #increment L bound with new window size. do it again
        #once L + size = len(nums), return saved window