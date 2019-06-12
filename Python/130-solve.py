class Solution1:
    '''
    DFS+回溯+递归
    '''

    def _dfs(self, board, x, y):
        if 0 <= x < self.row \
                and 0 <= y < self.col \
                and board[x][y] == 'O':
            board[x][y] = '*'
            for i in range(4):
                newx = x + self.d[i][0]
                newy = y + self.d[i][1]
                self._dfs(board, newx, newy)
        return


    def solve(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None

        self.row = len(board)
        self.col = len(board[0])
        self.d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        #  将第一列和最后一列的O变成*
        for i in range(self.row):
            self._dfs(board, i, 0)
            self._dfs(board, i, self.col - 1)
        #  将第一行和最后一行的O变成*
        for i in range(self.col):
            self._dfs(board, 0, i)
            self._dfs(board, self.row - 1, i)

        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'

if __name__ == '__main__':

    s = Solution1()
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    s.solve(board)
    print(board)
