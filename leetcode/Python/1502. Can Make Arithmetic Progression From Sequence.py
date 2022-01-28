class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort(reverse=True)
        li = []
        for i in range(len(arr) - 1):
            diff = arr[i] - arr[i+1]
            li.append(diff)

        ano = []
        it = li[0]
        for item in li:
            if item == it:
                ano.append(True)
            else:
                ano.append(False)
        return all(ano)
