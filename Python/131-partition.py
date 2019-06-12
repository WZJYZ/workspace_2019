class Solution:
    # 回溯

    res = []
    tmp = []
    def isPalindrome(self, s: str):
        return s == s[::-1]

    def dfs(self, s: str):
        '''

        :param s:
        :param index: 初始为0
        :return:
        '''
        if 0 == len(s):  # 递归终止条件，在res中保存tmp的复制值
            self.res.append(self.tmp.copy())
            # tmp.clear()
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[0:i]):
                self.tmp.append(s[0:i])
                self.dfs(s[i:])  # 进入下一次递归
                if self.tmp:    # 每次递归返回时pop tmp中保存的值
                    self.tmp.pop()
        return


    def partition(self, s: str):
        self.res.clear()
        self.tmp.clear()
        self.dfs(s)
        return self.res

s = Solution()
print(s.partition('cdd'))
