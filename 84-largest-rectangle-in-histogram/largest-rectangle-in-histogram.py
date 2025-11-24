class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)  # add a small bar to clear stack at the end
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)

        return max_area
