import random

l = []

for i in range(1,10):
    l.append(i)

l.remove(random.choice(l))
print(l)

for i in range(1,9):
    if l[i-1] != i:
        print(str(i)+' is the missing number')
        break
