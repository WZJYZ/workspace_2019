class Solution:
    def isValid(self, s):
        '''

        :param s:
        :return: bool
        '''

        res = []
        for ss in s:
            if ss == '(' or ss == '[' or ss == '{':
                res.append(ss)
            elif ss == ')':
                if len(res) != 0:
                    tmp = res.pop()
                    if tmp == '(':
                        continue
                    else:
                        return False
                else:
                    return False
            elif ss == ']':
                if len(res) != 0:
                    tmp = res.pop()
                    if tmp == '[':
                        continue
                    else:
                        return False
                else:
                    return False
            elif ss == '}':
                if len(res) != 0:
                    tmp = res.pop()
                    if tmp == '{':
                        continue
                    else:
                        return False
                else:
                    return False
        return len(res) == 0

s = Solution()
print(s.isValid(")"))