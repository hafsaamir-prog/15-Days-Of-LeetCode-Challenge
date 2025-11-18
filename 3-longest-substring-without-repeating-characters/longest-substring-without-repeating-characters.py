class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        seen = {}
        longest = 0
        for i, ch in enumerate(s):
            if ch in seen and seen[ch] >= start:
                start = seen[ch] + 1
            seen[ch] = i
            if i - start + 1 > longest:
                longest = i - start + 1
        return longest
