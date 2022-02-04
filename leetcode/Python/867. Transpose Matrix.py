class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(matrix[0])):
            level = []
            for j in range(len(matrix)):
                level.append(matrix[j][i])
            ans.append(level)

        return ans
