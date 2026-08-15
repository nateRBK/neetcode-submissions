class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iteration = 1
        N = len(nums)
        for i in range(0,N):
            for j in range(iteration,N):
                if nums[i] + nums[j] == target:
                    return [i,j]
            iteration += 1
                