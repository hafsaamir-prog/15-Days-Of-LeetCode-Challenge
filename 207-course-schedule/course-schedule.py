class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
        
        visit = [0] * numCourses
        
        def dfs(course: int) -> bool:
            if visit[course] == 1:
                return False
            if visit[course] == 2:
                return True
            
            visit[course] = 1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            
            visit[course] = 2
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
