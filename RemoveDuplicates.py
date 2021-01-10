import time

def RemoveDuplicate(array): #doesn't work with od number duplicates
    print(array)
    arr = []
    for i in array:
        dup = 0
        for j in array:
            if i == j and dup > 0:
                print(j)
                array.remove(j)
                continue
            elif i == j and dup == 0:
                dup = 1
                continue
    print(array)

def RemoveDuplicates2(array): #just the better method
    newArray = []
    [newArray.append(x) for x in array if x not in newArray]
    print(newArray)

def Remove3(array):
    return list(set(array))

array1 = [1,2,3,4,4,5,5,5,5,6]
array2 = [1,2,3,4,4,5,5,5,5,5,6]

start = time.time()
RemoveDuplicate(array1)
print(time.time()-start)

start = time.time()
RemoveDuplicate(array2)
print(time.time()-start)

start = time.time()
print(Remove3(array1))
print(time.time()-start)

#print(RemoveDuplicates2(array1))
