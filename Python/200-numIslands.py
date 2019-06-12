class Solution:

    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        def jugde( x, y):
            if x < 0 or x >= row or y < 0 or y >= col:
                return False
            if grid[x][y] == '0' or visited[x][y] == True:
                return  False
            return True

        def dfs(x, y):
            if not jugde(x, y):
                return
            visited[x][y] = True
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)

        ans = 0

        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1' and visited[x][y] == False:
                    ans += 1
                    dfs(x, y)
        return ans

s = Solution()
print(s.numIslands(['11110', '11010', '11000', '00000']))

