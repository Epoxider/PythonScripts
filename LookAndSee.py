def countstring(n):
    s = "1"
    index = 1

    while index < n:
        sl = []
        last_char = 'X'
        number_found = 0
        for c in s:
            if c != last_char and number_found > 0:
                sl.append(str(number_found))
                sl.append(last_char)
                number_found = 0
            last_char = c
            number_found += 1
        sl.append(str(number_found))
        #print("number found = " + str(number_found))
        sl.append(last_char)
        #print("last char = " + str(last_char))
        s = ''.join(sl)
        index += 1

    return s

for i in range(8):
    print(str(countstring(i+1)))
