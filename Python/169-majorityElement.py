class Solution1:
    #1.暴力求解
    def majorityElement(self, nums) -> int:
        '''

        :param nums: List[int]
        :return: int
        '''
        Max = 0
        res = nums[0]
        for i in range(len(nums)):
            count = 1
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    count += 1

            if count > Max:
                Max = count
                res = nums[i]
        if Max > int(len(nums))/2:
            return res
        else:
            return None

s = Solution1()
print(s.majorityElement([2,2,1,1,1,2,2]))

class Solution2:
    #1.使用map（值， 个数）
    def majorityElement(self, nums) -> int:
        '''

        :param nums: List[int]
        :return: int
        '''
        d = {}

        for num in nums:
            if num not in d: #判断num在字典中否？
                d[num] = 1
            else:
                d[num] += 1
        for k, v in d.items():
            if v > int(len(nums)/2):
                return k
        return None

s = Solution2()
print(s.majorityElement([1,1,1,2,2,2,2]))

class Solution3:
    #3.分治
    def majorityElement(self, nums) -> int:
        '''

        :param nums: List[int]
        :return: int
        '''
        n = len(nums)

        if  n == 1:
            return nums[n - 1]

        x = self.majorityElement(nums[0:int(n/2)]) #左闭右开区间[)
        y = self.majorityElement(nums[int(n/2):])

        if x == y:
            return x
        else:
            countX = 0
            countY = 0
            for i in range(n):
                if nums[i] == x:
                    countX += 1
                elif nums[i] == y:
                    countY += 1
            return x if countX > countY else y


s = Solution3()
print(s.majorityElement([3, 2, 3]))

class Solution4:
    #3.分治
    def majorityElement(self, nums) -> int:
        '''
        4.Boyer-Moore Voting Algorithm
        不是很懂
        :param nums: List[int]
        :return: int
        '''
        assert len(nums) > 0
        count = 0
        res = -1
        for num in nums:
            if count is 0:
                res = num
            if res == num:
                count += 1
            else:
                count -= 1
        return res

s = Solution4()
print(s.majorityElement([3, 2, 3]))