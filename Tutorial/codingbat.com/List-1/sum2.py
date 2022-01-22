def sum2(nums):
  n = len(nums)
  if n == 0 :
    return 0
  elif n < 2 :
    return nums[0]
  else :
    return nums[0] + nums[1]
