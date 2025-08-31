s = input("Enter the word:")
vowels = "AEIOUaeiou"
vow_count=0
const_count=0
for ch in s:
    if ch in vowels:
      vow_count += 1
    
    else:
      const_count+=1
    
print("Number of vowels:",vow_count)
print("Number of const :",const_count)