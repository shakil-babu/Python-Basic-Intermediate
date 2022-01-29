class Solution:
    def minPartitions(self, n: str) -> int:
        nums = []
        for item in n:
            nums.append(int(item))

        m = max(nums)
        return m
