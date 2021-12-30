def toHex(num):
    if num == 0:
        return "0"
    elif num < 0:
        posnum = (-1) * num

        # Decimal to Binary
        binarystr = bin(posnum).replace("0b","").zfill(32)  # .replace and .zfill make bin into str
        #print(binarystr)

        # 2's complement: (or use ~bin(posnum) instead of following)
        complement = ""
        for i in range(len(binarystr)):
            if binarystr[i] == "1":
                complement += "0"
            elif binarystr[i] == "0":
                complement += "1"
        combinary = bin(int(complement, 2) + int("1", 2)).replace("0b","")  # int(binary,2)=decimal
        #print(combinary)

        # Binary to Decimal:
        decinum = int(combinary, 2)
        #print(decinum)

        return decimalToHex(decinum)

    else:
        # Decimal to Hexadecimal:
        return decimalToHex(num)

def decimalToHex(num):
    tmp = ""
    while num >= 1:
        remainder = num % 16  # num = 26, remainder = 10; num=1,r=1
        if remainder < 10: #["a","1"]
            tmp += str(remainder)
        else:
            switcher = {
                10: "a",
                11: "b",
                12: "c",
                13: "d",
                14: "e",
                15: "f",
            }
            tmp += switcher[remainder]
        num = num // 16  # 1
    hexastr = tmp[::-1]
    return hexastr

num = -1
print(toHex(num))





