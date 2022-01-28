class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = dict()
        for item in nums:
            if dic.get(item):
                dic[item] += 1
            else:
                dic[item] = 1
        for item in dic.items():
            if item[1] == 1:
                return item[0]
