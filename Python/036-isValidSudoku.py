class Solution1:
    #1.暴力法
    def isValidSudoku(self, board) -> bool:
        rows = len(board)
        cols = len(board[0])

        #空间换时间
        import copy
        hashtable1 = [[0 for _ in range(rows)] for _ in range(cols)]
        hashtable2 = copy.deepcopy(hashtable1)
        hashtable3 = copy.deepcopy(hashtable1)

        #检查行
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    if hashtable1[i][num] == 1:
                        return False
                    hashtable1[i][num] = 1
        #检查列
        for j in range(cols):
            for i in range(rows):
                if board[j][i] != '.':
                    num = int(board[j][i]) - 1
                    if hashtable2[i][num] == 1:
                        return False
                    hashtable2[i][num] = 1

        #检查每个block
        for i in range(rows):
            br = i//3
            bc = i%3
            for ii in range(3):
                for jj in range(3):
                    r = br * 3 + ii
                    c = bc * 3 + jj
                    if board[r][c] != '.':
                        num = int(board[r][c]) - 1
                        if hashtable3[i][num] == 1:
                            return False
                        hashtable3[i][num] = 1
        return True

class Solution2:
    #1.暴力法
    def isValidSudoku(self, board) -> bool:
        rows = len(board)
        cols = len(board[0])

        # 空间换时间
        import copy
        rowFlag = [[False for _ in range(rows)] for _ in range(cols)]
        colFlag = copy.deepcopy(rowFlag)
        cellFlag = copy.deepcopy(rowFlag)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1

                    if rowFlag[i][num] or colFlag[num][j] or cellFlag[3*(i//3) + j//3][num]:
                        return False
                    rowFlag[i][num] = True
                    colFlag[num][j] = True
                    cellFlag[3*(i//3) + j//3][num] = True
        return True

s = Solution2()
a = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(a))

