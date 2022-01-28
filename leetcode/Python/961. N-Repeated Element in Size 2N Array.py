class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic = dict()
        for item in nums:
            if dic.get(item):
                dic[item] += 1
            else:
                dic[item] = 1

        items = dic.items()
        ab = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return ab[0][0]
