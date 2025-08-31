numbers = list(map(int, input("Enter the numbers: ").split()))
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1 
    else:
        freq[num] = 1    
print("Frequency of elements:", freq) 