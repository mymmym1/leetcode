def readBinaryWatch(turnedOn):
    output = []
    for h in range(12):
        for m in range(60):
            if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                t = f"{str(h)}:{str(m).zfill(2)}"  # f: format
                output.append(t)
    return output

turnedOn = 2
print(readBinaryWatch(turnedOn))

