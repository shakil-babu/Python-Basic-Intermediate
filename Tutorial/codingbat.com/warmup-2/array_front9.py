def array_front9(nums):
  n = len(nums)
  if n > 4 :
    n = 4
  for i in range(n):
    if nums[i] == 9:
      return True
  
  return False
