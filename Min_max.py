numbers= list(map(int,input("Enter numbers").split()))
smallest =numbers[0]
largest  = numbers[1]
for num in numbers:
    if num < smallest:
        smallest = num 
    elif num > largest:
        largest = num
print("Smallest number:", smallest)
print("largest number:", largest)
