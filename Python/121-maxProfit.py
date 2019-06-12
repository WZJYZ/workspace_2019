class Solution:
    #1.贪心法
    def maxProfit(self, prices):
        res = 0
        for i in range(len(prices)-1):
            if prices[i] >= prices[i+1]:
               continue
            else:
                res += prices[i+1]-prices[i]
        return res

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([7, 6, 4, 3, 1]))