class Solution:
    def findWord(self, M, N, board, word, coor, visit, idx, result):
        if idx == len(word):
            return True

        r, c = coor
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in dirs:
            dr += r
            dc += c
            if 0 <= dr < M and 0 <= dc < N and board[dr][dc] == word[idx] and not visit[dr][dc]:
                visit[dr][dc] = True
                result = self.findWord(M, N, board, word, [dr, dc], visit, idx+1, result)
                visit[dr][dc] = False

        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])

        for m in range(M):
            for n in range(N):
                if board[m][n] == word[0]:
                    visit = [[False] * N for _ in range(M)]
                    visit[m][n] = True
                    if self.findWord(M, N, board, word, [m, n], visit, 1, False):
                        return True

        return False
