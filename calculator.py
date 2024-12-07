# Basic Calculator Program
print('Please enter two numbers')
num1 = int(input('Your first number: '))
num2 = int(input('Your second number: '))

# Asking the user for the operator to use
operator = input('Please choose the operator for your calculation +, -, *, / ')

# Conditional statements to validate the operator and perform the appropriate arithmetic operation
if (operator == '+'):
  result = num1 + num2
elif (operator == '-'):
  result = num1 - num2
elif (operator == '*'):
  result = num1 * num2
elif (operator == '/'):
  if (num2 == 0):
    print('You can"t divide by 0')
  else:
    result = num1 / num2
else:
  print('Invalid Operator')

print(f'\n {num1} {operator} {num2} equals {result}')

