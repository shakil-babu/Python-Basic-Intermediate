# lambda function
nums = [1,2,3,4,5]
squred_nums = []

squre = lambda n : n *2
for item in nums:
    squred_nums.append(squre(item))

print(squred_nums)