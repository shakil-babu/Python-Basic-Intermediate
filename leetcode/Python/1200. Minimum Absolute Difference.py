class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        li = []
        for i in range(len(arr) - 1):
            dif = abs(arr[i+1] - arr[i])
            li.append(dif)

        minDiff = min(li)
        ans = []
        for i in range(len(arr) - 1):
            diff = abs(arr[i+1] - arr[i])
            if diff == minDiff:
                ans.append([arr[i], arr[i+1]])

        return ans
