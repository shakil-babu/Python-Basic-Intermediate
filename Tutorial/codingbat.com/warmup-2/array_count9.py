def array_count9(nums):
  counter = 0
  for item in nums :
    if item == 9 :
      counter = counter + 1
      
  return counter


"""
or

return nums.count(9)
"""