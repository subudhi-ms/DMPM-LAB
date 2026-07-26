# write a program to find the factorial of a number
num = int(input("Enter a number: "))
f = 1
for i in range(1, num + 1):
    f = f * i
print(f)