#write a program to check whether a string is a palindrome
text = input("Enter a string: ")
reverse = text[::-1]
if text == reverse:
    print("palindrome")
else:
    print("not palindrome")    