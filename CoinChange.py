def makeChange(money):
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1
    changeList = []

    quartersReturned = 0
    dimesReturned = 0
    nickelsReturned = 0
    penniesReturned = 0

    while money - quarter >= 0:
        if money == 0:
            return changeList
        changeList.append(quarter)
        quartersReturned += 1
        money -= quarter
    while money - dime >= 0:
        if money == 0:
            return changeList
        changeList.append(dime)
        dimesReturned += 1
        money -= dime 
    while money - nickel >= 0:
        if money == 0:
            return changeList
        changeList.append(nickel)
        nickelsReturned += 1
        money -= nickel
    while money - penny >= 0:
        if money == 0:
            return changeList
        penniesReturned += 1
        changeList.append(penny)
        money -= penny
    #print("You get "+str(quartersReturned)+" quarters \n")
    #print("You get "+str(dimesReturned)+" dimes \n")
    #print("You get "+str(nickelsReturned)+" nickels \n")
    #print("You get "+str(penniesReturned)+" pennies \n")
    return changeList

print(makeChange(37))
print(makeChange(1))
print(makeChange(0))
print(makeChange(25))
print(makeChange(67))
print(makeChange(100))
        
