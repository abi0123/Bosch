def left_rotate(arr,d):
    n=len(arr)
    d= d%n
    return arr[d:]+arr[:d]

arr=[1,2,3,4,5,6]
d=2
print("The given array:",arr)
print("Left roated array:",left_rotate(arr,d))

