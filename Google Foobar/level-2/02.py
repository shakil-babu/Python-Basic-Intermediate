# foorbar - Level(2) - second
def solution(l):
    result = sorted(l, key=lambda x: [int(i) for i in x.split('.')])
    return result


ans = solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
print(ans)
