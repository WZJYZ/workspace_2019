class Solution:
    #  组合问题，思路：回溯算法
    res = []


    def generateCombination(self, nums: int, k: int, start: int, tmp: list):

        if len(tmp) == k:
            self.res.append(tmp.copy())
            return

        # for i in range(start, nums+1):  # 未剪枝
        for i in range(start, nums + 1 - (k - len(tmp)) + 1):  # 剪枝
            tmp.append(i)
            self.generateCombination(nums, k, i + 1, tmp)
            tmp.pop()

        return

    def combine(self, n: int, k: int):
        self.res.clear()

        tmp = []
        self.generateCombination(n, k, 1, tmp)
        return self.res

s = Solution()
print(s.combine(4, 2))
