def log(n):
    if n == 0:
        return
    log(n-1)
    print(n)

log(10)