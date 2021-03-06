def calculate_apr():
  '''
  This function is used to calculate how much money can be made in an investment over time
  using the formula principal*(1+(interest_rate))
  '''
#both principal and interest_rate parameters are floats while years is in int
  principal = float(input())
  interest_rate = (float(input()) / 100)
  years = int(input())
  total = 0
  for i in range(years):
    total = total + (principal * (1 + (interest_rate))
                     
 #if any parameters are negative, return false
  if principal < 0:
    return False
  elif interest_rate < 0:
    return False
  elif years < 0:
    return False
  else:
    print(total)

calculate_apr()
