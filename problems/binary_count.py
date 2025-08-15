n = input("An integer value:")

b = bin(int(n))

count = 0
for i in b:
    if i=='1':
        count+=1
print("Number of one in its binary value:",count)
