class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for item in nums:
            if (item-1) not in nums: 
                #filtering for if first item in consecutive chain
                length = 1
                while (item + length) in nums:
                    #check for next number
                    length += 1
                    #check for number after that
                    #stop
                longest = max(length, longest)
                #compare record to this run
        return longest
        