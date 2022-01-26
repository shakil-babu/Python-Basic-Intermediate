def combo_string(a, b):
  s = a
  l = b
  if len(a) > len(b) :
    s = b
    l = a
  else :
    s = a
    l = b
  return s + l + s
  
