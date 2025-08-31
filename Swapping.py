num1 = int(input("Enter first numb:"))
num2 = int(input("Enter second numb:"))
numbers = [num1, num2]
print("After swapping",numbers)
numbers[0], numbers[1] = numbers[1], numbers[0]
print("After swapping",numbers)



