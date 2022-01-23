# # map method
# nums = [1,2,3,4,5]

# def multiple(num) :
#     return num*num

# ans = map(multiple, nums)

# # convert into list
# squre = list(ans)
# print(squre)


nums = [1,2,3,4,5]
ans = map(lambda x : x*x , nums)

# converting into list
squre = list(ans)
print(squre)