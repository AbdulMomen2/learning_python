print("*****Welcome to ABC Calculator*****")
print('')
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

num3 = input("Select operator: (+,-,*,/,%,//) : " )


if num3 == '+':
    print("Your magic number is: " , num1 + num2)
elif num3 == '-':
   print("Your magic number is: " , num1 - num2)
elif num3 == '*':
  print("Your magic number is: " , num1 * num2)
elif num3 == '/':
   print("Your magic number is: " , num1 / num2)
elif num3 == '%':
    print("Your magic number is: " , num1 % num2)
elif num3 == '//':
    print("Your magic number is: " , num1 // num2)
else:
    print('Sorry, Invalid operation')
