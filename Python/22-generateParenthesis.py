class Solution:
    '''

    def generateParenthesis(self, n):
        self.res = []
        self.singleStr('', 0, 0, n)
        return self.res

    def singleStr(self, s, left, right, n):
        if left == n and right == n:
            self.res.append(s)
        if left < n:
            self.singleStr(s + '(', left + 1, right, n)
        if right < left:
            self.singleStr(s + ')', left, right + 1, n)

    '''

    def generateParenthesis(self, n):
        '''


        ans = []
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                print(s)
                backtrack(s+"(", left+1, right)
                print(s)
            if right < left:
                print(s)
                backtrack(s+')', left, right+1)
                print(s)
        backtrack()
        return ans

        '''

        def generate(A=[]):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

class Solution2:
    def generateParenthesis(self, n):
        self.list = []
        self._gen(0, 0, n, "")
        return self.list

    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)
        if left < n:
            self._gen(left + 1, right, n, result + "(")

        if left > right and right < n:
            self._gen(left, right + 1, n, result + ")")




s = Solution2()
res = s.generateParenthesis(3)

print(res)