def ans(n):
    binary = bin(n).replace("0b", "")
    num = ""
    for item in binary:
        if item == "0":
            num += "1"
        else:
            num += "0"

    num = int(num, 2)
    return num


res = ans(5)
print(res)
