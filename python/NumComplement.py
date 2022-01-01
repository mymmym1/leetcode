def findComplement(num):
    binarystr = bin(num).replace("0b","")
    newstr = ""
    for i in range(len(binarystr)):
        if binarystr[i] == '0':
            newstr += '1'
        elif binarystr[i] == '1':
            newstr += '0'
    newInt = int(newstr, 2)
    return newInt

num = 5
num = 1
print(findComplement(num))