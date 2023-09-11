from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])

        result = []
        for m in range(M):
            for n in range(N):
                q = deque([[m,n]])
                visit = [[False]*N for _ in range(M)]
                visit[m][n] = True

                ocean = [False, False]
                while q:
                    r, c = q.popleft()
                    if not r or not c:
                        ocean[0] = True
                    if r == M-1 or c == N-1:
                        ocean[1] = True

                    if ocean[0] and ocean[1]:
                        result.append([m,n])
                        break
                        
                    dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
                    for dr, dc in dirs:
                        dr += r
                        dc += c
                        if 0 <= dr < M and 0 <= dc < N and not visit[dr][dc]:
                            if heights[dr][dc] <= heights[r][c]:
                                q.append([dr,dc])
                                visit[dr][dc] = True

        return result
