class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            if heights[0] < heights[1]:
                return heights[0]
            else:
                return heights[1]
        m = 0
        L,R = 0,len(heights)-1
        while L < R:
            if heights[L] < heights[R]:
                h = heights[L]
            else:
                h = heights[R]

            if (R-L) * h > m:
                m = (R-L) * h

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return m