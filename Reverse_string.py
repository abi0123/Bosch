str = input("Enter a string:")
reversed_string= str[::-1]
print(reversed_string)


#using recursion
def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return reverse_string(s[1:])+s[0]

s = input("Enter the string:")
result =reverse_string(s)
print(result)
    
