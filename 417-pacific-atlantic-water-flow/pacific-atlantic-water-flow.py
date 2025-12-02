class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c, visited):
            visited.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if heights[nr][nc] >= heights[r][c]:
                        if (nr, nc) not in visited:
                            dfs(nr, nc, visited)
        
        for c in range(n):
            dfs(0, c, pacific)
        for r in range(m):
            dfs(r, 0, pacific)
        for c in range(n):
            dfs(m-1, c, atlantic)
        for r in range(m):
            dfs(r, n-1, atlantic)
        result = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result
