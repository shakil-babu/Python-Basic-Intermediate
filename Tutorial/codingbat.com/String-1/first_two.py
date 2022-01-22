def first_two(str):
  n = len(str)
  if n == 0:
    return ""
  elif n <= 2 :
    return str
  else :
    return str[:2]