class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = set(), set()
        n_row, n_col = len(matrix), len(matrix[0])
        for i in range(n_row):
            for j in range(n_col):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for r in row:
            for c in range(n_col):
                matrix[r][c] = 0

        for c in col:
            for r in range(n_row):
                matrix[r][c] = 0

        return matrix
