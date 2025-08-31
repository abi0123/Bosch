n1 = int(input("Enter number of items dict_1: "))
dict1 = {}
for i in range(n1):
    key = input("Enter key  for dict1: ")
    value = input("Enter value for key ")
    dict1[key] = value
n2 = int(input("Enter number of items dict_2: "))
dict2 = {}
for i in range(n2):
    key = input("Enter key for dict2: ")
    value = input("Enter value for key ")
    dict2[key] = value
merged_dict = dict1.copy()
merged_dict.update(dict2)
print(merged_dict)



































































