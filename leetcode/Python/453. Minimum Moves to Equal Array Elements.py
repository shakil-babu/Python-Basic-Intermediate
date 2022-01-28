class Solution:
    def minMoves(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        moves, i = 0, 1
        while i < len(arr):
            moves += (arr[i-1] - arr[i]) * i
            i += 1

        return moves
