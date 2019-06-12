'''
使用一个栈作为辅助，遍历数字字符串，当当前的字符比栈最后的字符小的时候，说明要把栈的最后的这个字符删除掉。为什么呢？你想，把栈最后的字符删除掉，然后用现在的字符进行替换，是不是数字比以前的那种情况更小了？所以同样的道理，做一个while循环！这个很重要，可是我没有想到。在每一个数字处理的时候，都要做一个循环，使得栈里面最后的数字比当前数字大的都弹出去。

最后，如果K还没用完，那要删除哪里的字符呢？毋庸置疑肯定是最后的字符，因为前面的字符都是小字符。
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/81034522
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
class Solution:
    #使用栈
    def removeKdigits(self, num, k):
        res = []

        for ch in num:
            while res and k > 0 and ch < res[-1]:
                res.pop()
                k -= 1
            res.append(ch)

        while k:
            res.pop()
            k -= 1

        #去掉前导0
        while res and res[0] == '0':
            res.remove(res[0])

        if not res:
            return '0'
        else:
            return ''.join(res) #join函数的使用
        #return res if res else '0'
s = Solution()
print(s.removeKdigits('112', 1))