# Solution.py

class Solution:
    def maxSubArray(self, nums):
        """
        Kadane's algorithm (simple and O(n)).
        Returns the largest sum of any contiguous subarray.
        """
        # constraints guarantee len(nums) >= 1
        current_sum = nums[0]
        max_sum = nums[0]

        for n in nums[1:]:
            # either start new at n or extend the current subarray
            current_sum = max(n, current_sum + n)
            # update the global maximum
            max_sum = max(max_sum, current_sum)

        return max_sum


# Optional: local test harness. Leave it — it won't affect online judge drivers
if __name__ == "__main__":
    examples = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1], 1),
        ([5,4,-1,7,8], 23),
    ]

    s = Solution()
    for arr, expected in examples:
        result = s.maxSubArray(arr)
        print(f"nums = {arr}\n -> result = {result} (expected {expected})\n")
