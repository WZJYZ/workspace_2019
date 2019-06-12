class Solution:
    def twoSum(self, nums, target):
        items = {}
        res = []
        for i in range(len(nums)):
            items[nums[i]] = i

        for i in range(len(nums)):
            temp = target - nums[i]
            if items.get(temp) and items[temp] != i:
                res.append(i)
                res.append(items[temp])
                break
        return res
