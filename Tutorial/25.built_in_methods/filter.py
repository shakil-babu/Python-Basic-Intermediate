# numbers = [1,2,3,4,5,6]

# # return True if number is even
# def check_even(number) :
#     if number % 2 == 0:
#         return True
    
#     return False


# nums = filter(check_even, numbers)
# evenNums = list(nums)
# print(evenNums)


# using lambda function
numbers  =[1,2,3,4,5]
arr = filter(lambda x : x%2 == 0, numbers)

# conver
even = list(arr)
print(even)


