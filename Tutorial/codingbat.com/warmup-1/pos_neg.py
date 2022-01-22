def pos_neg(a, b, negative):
  if a<0 and b < 0 and negative == True :
    return True
  elif negative == False and (a < 0 or b < 0 ) and (a>0 or b > 0 ) :
    return True
  else :
    return False
