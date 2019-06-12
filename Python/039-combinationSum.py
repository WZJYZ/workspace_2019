class Solution:

    res = []

    def find(self, candidates: list, index: int, target: int, tmp: list):
        '''

        :param candidates:
        :param index: 用来防止重复，每次递归都只能从当前的index开始
        :param target:
        :param tmp:
        :return:
        '''
        if target == 0:
            self.res.append(tmp.copy())
            return
        for i in range(index, len(candidates)):
            if candidates[i] <= target:
                tmp.append(candidates[i])
                self.find(candidates, i, target - candidates[i], tmp)
                tmp.pop()
    def combinationSum(self, candidates: list, target: int):
        self.res.clear()
        tmp = []
        self.find(candidates, 0, target, tmp)
        return self.res

s = Solution()
print(s.combinationSum([2, 3, 5], 8))