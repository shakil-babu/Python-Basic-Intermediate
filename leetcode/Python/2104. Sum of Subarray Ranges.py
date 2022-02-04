class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            Min, Max = nums[i], nums[i]

            for j in range(i, n, 1):
                Min = min(Min, nums[j])
                Max = max(Max, nums[j])
                result -= Max - Min

        return abs(result)
