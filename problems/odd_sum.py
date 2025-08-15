n = input("Number of elements in an array/list:")

arr = input("Elements of the list/array:").split()

sum=0
for i in arr:
    if int(i)%2==1:
        sum+=int(i)

print(sum)

