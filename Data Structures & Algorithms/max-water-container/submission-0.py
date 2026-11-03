class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start at both sides
        # compute the area
        # comapre the pointers
        # move the shorter pointer
        # computer the area
        # repeat until l = r
        max_area = 0
        L,R = 0,len(heights) - 1 # index
        l,r = heights[L], heights[R] # value
        while L < R:
            l,r = heights[L], heights[R]
            width = R - L
            if r > l:
                area = width * l
                L += 1
                max_area = max(max_area,area)
            else:
                area = width * r
                R -= 1
                max_area = max(max_area,area)
                
        return max_area




