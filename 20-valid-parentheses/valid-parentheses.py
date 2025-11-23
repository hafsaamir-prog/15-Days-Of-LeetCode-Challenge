class Solution:
    def isValid(self, s):
        stack = []

        for ch in s:
            if ch in "([{":
                stack.append(ch)

            else:  # it's a closing bracket
                if not stack:      # nothing to match
                    return False

                last = stack.pop() # remove last opened bracket

                if ch == ')' and last != '(':
                    return False
                if ch == ']' and last != '[':
                    return False
                if ch == '}' and last != '{':
                    return False

        return len(stack) == 0
