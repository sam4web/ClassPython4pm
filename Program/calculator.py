firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))

if firstNum != 0 and secondNum != 0:
    o = input("Enter + - * /: ")
    if o == '+':
        print(firstNum + secondNum)
    elif o == '-':
        print(firstNum - secondNum)
    elif o == '*':
        print(firstNum * secondNum)
    elif o == '/':
        print(firstNum / secondNum)
    else:
        print("Invalid operator.")
else:
    print("Zero is invalid.")
