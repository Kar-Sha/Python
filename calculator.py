def calculator(number1, number2, operator):
  '''
  This function acts as a calculator and prints a result 
  depending on the number1 and number2 variables as well as the operator
  '''
  if operator == "+":
    print(number1 + number2)
  elif operator == "-":
    print(number1 - number2)
  elif operator == "*":
    print(number1 * number2)
  elif operator == "/":
    print(number1 / number2)
  elif operator == "//":
    print(number1 // number2)
  elif operator == "**":
    print(number1 ** number2)
  elif operator == "%":
    print(number1 % number2)
  else:
    return False

def input_output():
 #This function is used to get input values for our numbers and operator 
  number1 = float(input("What is the first number: "))
  number2 = float(input("What is the second number: "))
  operator = input("Enter operation: ")
  print(calculator(number1, number2, operator))
  next = input("Do you want to continue: ")

  #asks is the user wants to continue when input is "y", and it stops running when input is "n"
  while(next == "y"):
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operator = input("Enter the operation: ")
    print(calculator(number1, number2, operator))
    next = input("Do you wish to exit: ")

    if next == "n":
      break

input_output()
