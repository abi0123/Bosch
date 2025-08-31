s = input('Enter the string:')
s = s.lower().replace(" ","")
if s == s[::-1]:
    print("The string is a Palindrome")
else:
    print("This is not a Palindrome")
