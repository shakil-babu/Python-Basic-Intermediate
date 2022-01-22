def fac(n):
    if n == 1:
        return n
    else :
        return n*fac(n-1)

ans = fac(5)
print(ans)