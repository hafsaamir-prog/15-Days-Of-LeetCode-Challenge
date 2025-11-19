class Solution:
    def maxSubArray(self, nums):
        # Kadane's Algorithm
        current_sum = nums[0]
        max_sum = nums[0]

        for n in nums[1:]:
            current_sum = max(n, current_sum + n)
            max_sum = max(max_sum, current_sum)

        return max_sum


# Optional test block (safe for Python 2)
if __name__ == "__main__":
    s = Solution()

    examples = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1], 1),
        ([5,4,-1,7,8], 23)
    ]

    for arr, expected in examples:
        result = s.maxSubArray(arr)
        print("nums =", arr)
        print("result =", result, " expected =", expected)
        print("")
