# 168. Excel Sheet Column Title
def convertToTitle(columnNumber):
    alphabetic = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    columnTitle = ""

    while columnNumber / 26 > 26:
        lastIndex = columnNumber % 26
        columnTitle += alphabetic[lastIndex - 1]
        columnNumber = columnNumber // 26

    if columnNumber >= 26:
        lastIndex = columnNumber % 26
        columnTitle += alphabetic[lastIndex - 1]
        if lastIndex != 0:
            lastsecondIndex = columnNumber // 26
            columnTitle += alphabetic[lastsecondIndex - 1]

    elif 1 <= columnNumber < 26:
        lastIndex = columnNumber % 26
        columnTitle += alphabetic[lastIndex - 1]

    else:
       title = "Illegal column number!"
       return title

    return columnTitle[::-1]

columnNumber = 2147483647
print(convertToTitle(columnNumber))
