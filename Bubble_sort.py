num = list(map(int, input("Enter the numbers: ").split()))
for i in range(0,len(num)-1):
    for j in range(0,len(num)-1):
        if num[j]<num[j+1]:
            continue
        elif num[j]>num[j+1]:
            k = num[j]
            num[j]=num[j+1]
            num[j+1] = k
    print(num)
