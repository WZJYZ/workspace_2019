class Solution:
    # 回溯算法
    res = list()  # 保存结果
    used = []
    def generatePermutation(self, nums: list, index: int, p: list):
        if index == len(nums):
            self.res.append(p.copy())
            return

        for i in range(len(nums)):
            if not self.used[i]:
                self.used[i] = True
                p.append(nums[i])
                self.generatePermutation(nums, index + 1, p)
                p.pop()
                self.used[i] = False

        # return


    def permute(self, nums: list):
        self.res.clear()
        if len(nums) == 0:
            return self.res
        self.used = [False for _ in range(len(nums))]
        p = []
        self.generatePermutation(nums, 0, p)
        return self.res

s = Solution()
print(s.permute([1, 1, 2]))