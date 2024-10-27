# 12. Develop a Python program to check if a given string is a palindrome.

string = input(" enter the string: ").lower()

palindrome= string[::-1]

if palindrome == string:
    print(" palindrome ")
else:
    print(" not palindrome ")