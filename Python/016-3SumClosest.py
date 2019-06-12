class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dic = {}
        for i in range(len(nums)-2): #固定i值
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < target:
                    l += 1
                    dic[sum] = target -sum #保存目标值域当前sum的差值
                elif sum > target:
                    r -= 1
                    dic[sum] = sum - target
                else:
                    return target
        return min(dic, key=dic.get) #找出与目标值差值最小的值的key





s = Solution()
nums = [-1, 2, 1, -4]
target = 1
res = s.threeSumClosest(nums, target)
print(res)