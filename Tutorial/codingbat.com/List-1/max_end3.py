def max_end3(nums):
  if nums[0] > nums[-1]:
    a = nums[0]
    return [a,a,a]
  else :
    return [nums[-1], nums[-1], nums[-1]]