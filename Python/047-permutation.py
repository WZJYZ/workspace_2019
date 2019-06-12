class Solution1:
    # 回溯算法
    res = list()  # 保存结果
    used = []
    def generatePermutation(self, nums: list, index: int, p: list):
        if index == len(nums):
            if p not in self.res:
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

class Solution2:
    # 回溯算法, 先对数组进行排序，如[1, 1, 2], 然后跳过相同的值如[1]
    res = list()  # 保存结果
    used = []
    def generatePermutation(self, nums: list, index: int, p: list):
        if index == len(nums):
            self.res.append(p.copy())
            return

        for i in range(len(nums)):
            if not self.used[i]:
                if (i > 0) and (nums[i] == nums[i-1]) and (not self.used[i-1]):
                    continue
                self.used[i] = True
                p.append(nums[i])
                self.generatePermutation(nums, index + 1, p)
                p.pop()
                self.used[i] = False

        # return


    def permuteUnique(self, nums: list):
        self.res.clear()
        if len(nums) == 0:
            return self.res
        self.used = [False for _ in range(len(nums))]
        p = []
        nums = sorted(nums)
        self.generatePermutation(nums, 0, p)
        return self.res

s = Solution2()
print(s.permuteUnique([1, 1, 2]))