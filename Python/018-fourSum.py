'''
思路：双指针法
1.排序
2.i, j固定两个值
3.左右指针移动
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = list()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                left = j + 1
                right = n - 1
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target and ([nums[i], nums[j], nums[left], nums[right]] not in res):
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif tmp < target:
                        left += 1
                    else:
                        right -= 1
        return res

s = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
res = s.fourSum(nums, target)
print(res)