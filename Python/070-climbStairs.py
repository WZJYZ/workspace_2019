class Solution1:
    #
    #斐波那契数列
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

class Solution2:
    #
    #动态规划
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)#空间换时间
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] #递推方程
        return dp[n]

class Solution3:

    '''
    分析：一次走一阶，也可以一次走两阶。
    到第n阶的总总走法数 = 到第n-1阶的走法数 + 到第n - 2 阶的总走法数。
    '''
    def climbStairs(self, n):
        if n == 0 or n == 1 or n == 2:
            return n
        dp = [0] * n # dp状态的定义
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2] # dp方程
        return dp[n - 1]


s = Solution3()
print(s.climbStairs(5))