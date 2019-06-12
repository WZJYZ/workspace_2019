class Solution:
    '''
    DFS+剪枝
    '''
    def solveNQueens(self, n: int):
        if n < 1:
            return []
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()

        self._DFS(n, 0, [])
        return self._generate_result(n)

    def _DFS(self, n, row, cur_state):
        '''

        :param n:
        :param row:
        :param cur_state: []
        :return:
        '''
        if row >= n:
            self.result.append(cur_state)
            return

        for col in range(n):
            if col in self.cols or col + row in self.pie or row - col in self.na:
                continue

            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self._DFS(n, row+1, cur_state+[col])

            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def _generate_result(self, n):

        return [ ['.'*i + 'Q' + '.'*(n - i - 1) for i in sol] for sol in self.result]


s = Solution()
print(s.solveNQueens(4))