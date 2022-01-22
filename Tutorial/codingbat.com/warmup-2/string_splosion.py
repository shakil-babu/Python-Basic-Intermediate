def string_splosion(str):
  ans = ""
  level = ""
  for i in range(len(str)):
    level += str[i]
    ans += level
    
  return ans
