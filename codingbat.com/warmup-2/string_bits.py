def string_bits(str):
  ans = ""
  n = len(str)
  for i in range(0,n,2):
    ans += str[i]
    
  return ans
