primary = input("primary String:").lower()
anagram = input("Anagram of primary String:").lower()

primary_list = []
shown = 0
for c in primary:
    if c == ' ':
        continue
    primary_list.append(c)

for i in anagram:
    if i == ' ':
        continue
    if i in primary_list:
        primary_list.remove(i)
    else:
        print("NO")
        shown = 1
        break

if primary_list==[] and shown==0:
    print("YES")
    shown=1

if shown==0:
    print("NO")
