def count_evens(nums):
  count = 0
  for item in nums:
    if item % 2 == 0 :
      count += 1
      
  return count
