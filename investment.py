def calculate_apr(principal, interest_rate, years):
  '''
  This function is used to calculate how much money can be made in an investment over time
  with the principal, interest_rate, and years parameters that are then 
  being used in the formula principal*(1+(interest_rate))
  '''
  #if any parameters are negative, return false
  if principal < 0:
    return False
  if interest_rate < 0:
    return False
  if years < 0:
    return False
  total = 0
  #loop by how many times the years value is
  for i in range(years):
    total = total + (principal * (1 + (interest_rate))
  return float(total)
calculate_apr()
