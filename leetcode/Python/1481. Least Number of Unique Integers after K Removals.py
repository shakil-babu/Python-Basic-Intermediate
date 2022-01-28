class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = dict()
        for item in arr:
            if dic.get(item):
                dic[item] += 1
            else:
                dic[item] = 1
        values = sorted(dic.values())
        n = len(values)
        for item in values:
            if k >= item:
                k = k - item
                n = n - 1
        return n
