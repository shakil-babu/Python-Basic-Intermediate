class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for item in matrix:
            for i in range(len(item)):
                if item[i] == target:
                    return True

        return False
