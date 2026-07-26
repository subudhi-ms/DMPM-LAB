# write a program to implement a simple calculator
a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
oper=input("Enter operator (+, -, *, %): ")
if oper=='+':
    print("addition is:", a + b)
elif oper=='-':
    print("subtraction is:", a - b)
elif oper=='*':
    print("multiplication is:", a * b)
elif oper=='%':
    print("modulus is:", a % b)