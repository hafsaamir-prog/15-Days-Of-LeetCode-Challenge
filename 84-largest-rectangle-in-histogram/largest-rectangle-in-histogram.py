from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        O(n) monotonic increasing stack solution.
        We iterate indices 0..n (treating index n as a sentinel height 0).
        """
        n = len(heights)
        stack = []           # will store indices of bars in increasing height order
        max_area = 0

        for i in range(n + 1):
            # current height is 0 when i == n to flush the stack
            cur_h = 0 if i == n else heights[i]

            # Pop while the stack top bar is taller than current bar
            while stack and heights[stack[-1]] > cur_h:
                h = heights[stack.pop()]
                # width: if stack empty => i, else => i - stack[-1] - 1
                width = i if not stack else i - stack[-1] - 1
                area = h * width
                if area > max_area:
                    max_area = area

            stack.append(i)

        return max_area


# Example usage (for local testing)
if __name__ == "__main__":
    example1 = [2,1,5,6,2,3]
    example2 = [2,4]
    print(Solution().largestRectangleArea(example1))  # -> 10
    print(Solution().largestRectangleArea(example2))  # -> 4
