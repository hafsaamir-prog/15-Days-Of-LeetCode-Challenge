class Solution:
    def hasCycle(self, head):
        visited = set()

        current = head
        while current:
            if current in visited:   # we've seen this node before
                return True
            visited.add(current)     # mark node as seen
            current = current.next

        return False

        