class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        for item in nums:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1
        for i in range(k):
            m = max(d, key = d.get)
            res.append(m)
            d.pop(m)
        return res