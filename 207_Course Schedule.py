from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        courses = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            indegree[a] += 1
            courses[b].append(a)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        n_take = 0
        while q:
            n_take += 1
            course = q.popleft()

            for c in courses[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        return True if n_take == numCourses else False
