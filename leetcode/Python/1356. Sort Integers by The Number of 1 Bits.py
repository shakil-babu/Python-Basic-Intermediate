class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda k: (bin(k)[2:].count('1'), k))
        return arr
