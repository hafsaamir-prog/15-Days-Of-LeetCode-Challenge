class Solution(object):
    def lengthOfLongestSubstring(self, s):
        window = []
        longest = 0
        for ch in s:
            if ch in window:
                i = window.index(ch)
                window = window[i+1:]
            window.append(ch)
            if len(window) > longest:
                longest = len(window)
        return longest
