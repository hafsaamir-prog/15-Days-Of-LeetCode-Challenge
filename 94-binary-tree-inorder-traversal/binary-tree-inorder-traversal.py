class Solution:
    def inorderTraversal(self, root):
        stack = []
        result = []
        current = root

        while current or stack:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Visit the node
            current = stack.pop()
            result.append(current.val)

            # Go to the right subtree
            current = current.right

        return result
