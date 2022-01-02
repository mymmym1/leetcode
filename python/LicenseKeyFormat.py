def licenseKeyFormatting(s, k):
    news = ""
    for i in range(len(s)):
        if s[i].isalpha():
            news += s[i].upper()
        elif s[i] == '-':
            news += ''
        elif s[i].isdigit():
            news += s[i]

    if k >= len(news):
        return news
    else:
        l = len(news) - 1
        result = ""
        n = 1
        while l >= 0:
            if len(news) - n * k > 0:
                if l != len(news) - n * k - 1:
                    result += news[l]
                    l -= 1
                else:
                    result += '-'
                    n += 1
            else:
                result += news[l]
                l -= 1
    return result[::-1]

s = "5F3Z-2e-9-w"
k = 4
s = "2-5g-3-J"
k = 2
print(licenseKeyFormatting(s, k))
