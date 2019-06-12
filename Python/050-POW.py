class Solution1:
    #1.使用函数
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)

class Solution2:
    #2.暴力
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for i in range(abs(n)):
            if n > 0:
                res *= x
            else:
                res /= x
        return res

class Solution3:
    #3.分治
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2: #n为奇数，res = x*y*y
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2) #n为偶数，res = y*y