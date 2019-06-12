class Solution:


    def inArea(self, x, y):
        return x >= 0 and x < self.m \
               and y >= 0 and y < self.n

    def searchWord(self, board, word, index, startx, starty):
        '''

        :param board:
        :param word:
        :param index:
        :param startx:
        :param starty:
        :return:bool
        '''
        if index == len(word) - 1:
            return board[startx][starty] == word[index]

        if board[startx][starty] == word[index]:
            self.visited[startx][starty] = True
            for i in range(4):
                newx = startx + self.d[i][0]
                newy = starty + self.d[i][1]

                if self.inArea(newx, newy) \
                        and not self.visited[newx][newy] \
                        and self.searchWord(board, word, index + 1, newx, newy):
                    return True
            self.visited[startx][starty] = False
        return False


    def exist(self, board: list, word: str):

        self.m = len(board)
        self.n = len(board[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for i in range(self.m):
            for j in range(self.n):
                if self.searchWord(board, word, 0, i, j):
                    return True

        return False

s = Solution()
board = \
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(s.exist(board, 'ABCB'))