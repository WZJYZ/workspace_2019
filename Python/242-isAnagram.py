class Solution:
    def isAnagram1(self, s, t):
        return sorted(s) == sorted(t)


    def isAnagram2(self, s, t):
        dict1, dict2 = {}, {}
        for item in s:
            dict1[item] = dict1.get(item, 0) + 1 #dict1.get(item, 0) ,存在item，返回其个数，不存在返回默认值0
        for item in t:
            dict2[item] = dict2.get(item, 0) + 1
        return dict2 == dict1
    def isAnagram(self, s, t):
        dict1, dict2 = [0]*26, [0]*26
        for item in s:
            dict1[ord(item) - ord('a')] += 1 #ord()返回字符对应的ASCII值
        for item in t:
            dict2[ord(item) - ord('a')] += 1
        return dict1 == dict2