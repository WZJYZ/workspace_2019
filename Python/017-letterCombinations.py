'''
回溯算法的实现包括递归和迭代
1.使用字典进行存储
2.使用递归进行组合
'''
import time

class Solution(object):

    def letterCombinations(self, digits):

        lookup = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        res = []

        def helper(s, digits):
            if len(digits) == 0:
                res.append(s)
            else:
                cur_digit = digits[0]
                for char in lookup[cur_digit]:
                    helper(s+char, digits[1:])
        if not digits or len(digits) == 0:
            return res
        helper('', digits)
        return res

class Solution2:
    # 回溯算法

    '''


    def __init__(self):
        self.res = []
        self.letterMap = [
            '', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'
        ]
        '''
    res = []
    letterMap = [
        '', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'
    ]
    def findCombination(self, digits, index, string):
        '''

        :param digits: 输入的数字，‘23’
        :param index: 数字索引
        :param string:
        :return:
        '''

        if index == len(digits):
            self.res.append(string)
            return
        c = digits[index]
        letters = self.letterMap[int(c)]
        for i in range(len(letters)):
            self.findCombination(digits, index + 1, string + letters[i])

        # return

    def letterCombinations(self, digits):
        self.res.clear()
        if digits == '':
            return self.res
        self.findCombination(digits, 0, '')
        return self.res

if __name__ == '__main__':
    start = time.time()
    s = Solution2()
    end = time.time()
    print(end - start)
    print(s.letterCombinations('23'))