
class Solution1:

    '''
    1. 动态规划,从顶往下
    '''
    def minimumTotal(self, triangle) -> int:
        minPath = triangle
        n = len(triangle)

        for i in range(1, n): # 从第一行到最后一行
            for j in range(0, len(triangle[i])): # 从第一列到每行最后一列
                # 到每行第一个节点和最后一个节点的路径只有一条
                if j == 0:
                    minPath[i][j] = triangle[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    minPath[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
                # 中间节点，等于上一层两个节点分别和当前节点相加的最小值
                else:
                    minPath[i][j] = min(triangle[i - 1][j - 1] + triangle[i][j],
                                    triangle[i - 1][j] + triangle[i][j])
        # 返回最后一层节点中保存的最小值
        return min(minPath[n - 1])

class Solution2:

    '''
    2. 动态规划,从低往上
    '''
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        minPath = triangle[n - 1] # 最底层所有数据

        # 从倒数第二层开始往上递推到第一层
        for i in range(n - 2, -1, -1): # 必须加上步长-1
            for j in range(0, len(triangle[i])):
                minPath[j] = triangle[i][j] + min(minPath[j], minPath[j + 1])

        return minPath[0]


s = Solution2()

t = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(s.minimumTotal(t))