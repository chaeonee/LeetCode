class Solution:
    def move(self, start, end, matrix):
        result = []
        for c in range(start[1], end[1]+1):
            result.append(matrix[start[0]][c])
        
        for r in range(start[0]+1, end[0]+1):
            result.append(matrix[r][end[1]])

        for c in range(end[1]-1, start[1]-1, -1):
            if start[0] == end[0]:
                break
            result.append(matrix[end[0]][c])
        
        for r in range(end[0]-1, start[0], -1):
            if start[1] == end[1]:
                break
            result.append(matrix[r][start[0]])

        return result


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = c = 0
        result = []
        n_row, n_col = len(matrix), len(matrix[0])
        while n_row > 0 and n_col > 0:
            result += self.move([r,c], [r+n_row-1, c+n_col-1], matrix)

            r += 1
            c += 1
            n_row -= 2
            n_col -= 2

        return result
