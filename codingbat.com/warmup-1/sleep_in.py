def sleep_in(weekday, vacation):
  if weekday == True and vacation == True :
    return True
    
  if weekday == False and vacation == False :
    return True
    
  if weekday == False and vacation == True :
    return True
  else :
    return False