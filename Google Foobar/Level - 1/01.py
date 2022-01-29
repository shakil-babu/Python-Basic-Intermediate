# foobar - level (1)

def solution(x, y):
    s1 = set(x)
    s2 = set(y)

    findUnCommonNumbers = s1.symmetric_difference(s2)
    final = list(findUnCommonNumbers)
    return final[0]


ans = solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
print(ans)
