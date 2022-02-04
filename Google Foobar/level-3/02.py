
def path(a, b, map):
    w = len(map[0])
    h = len(map)
    board = [[None for i in range(w)] for i in range(h)]
    board[a][b] = 1

    arr = [(a, b)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            nx, ny = x + i[0], y + i[1]
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] is None:
                    board[nx][ny] = board[x][y] + 1
                    if map[nx][ny] == 1:
                        continue
                    arr.append((nx, ny))

    return board


def solution(map):
    w = len(map[0])
    h = len(map)
    tb = path(0, 0, map)
    bt = path(h-1, w-1, map)

    ans = 2 ** 32-1
    for i in range(h):
        for j in range(w):
            if tb[i][j] and bt[i][j]:
                ans = min(tb[i][j] + bt[i][j] - 1, ans)
    return ans
