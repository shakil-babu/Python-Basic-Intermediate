def parrot_trouble(talking, hour):
  if talking == True and (hour <= 6 or hour > 20) :
    return True
  else :
    return False
