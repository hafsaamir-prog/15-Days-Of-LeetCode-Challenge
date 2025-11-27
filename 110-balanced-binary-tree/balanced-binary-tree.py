class Solution:
    def isBalanced(self, root):
        
        def check(node):
            if not node:
                return 0       # height = 0

            left = check(node.left)
            if left == -1:
                return -1     # left side not balanced

            right = check(node.right)
            if right == -1:
                return -1     # right side not balanced

            # If difference more than 1 → unbalanced
            if abs(left - right) > 1:
                return -1

            # return height of this subtree
            return 1 + max(left, right)

        return check(root) != -1
