class Solution:
    # 回溯算法

    def isValid(self, s: str):

        if len(s.strip()) == 0 or len(s.strip()) > 3 or (len(s.strip()) > 1 and s[0] is '0'):
            return False
        return 0 <= int(s.strip()) <= 255

    def restore(self, s: str, k: int, out: str, res: list):
        if k == 0:
            if len(s) == 0:
                res.append(out)
                return
            else:
                return
        print('out1:', out)
        for i in range(1, 4): # 1, 2, 3
            if len(s) >= i and self.isValid(s[0:i]):
                if k == 1:
                    self.restore(s[i:], k - 1, out + s[0:i], res)  # 前三次不需要加‘.’
                else:
                    self.restore(s[i:], k - 1, out + s[0:i] + '.', res)  # 最后一次之前加‘.’
                print('out2:', out)

        print('out4:', out)
        # return
    def restoreIpAddresses(self, s: str):
        res = []
        self.restore(s, 4, "", res)
        return res


s = Solution()
print(s.restoreIpAddresses('25525511135'))
print(s.isValid('333'))