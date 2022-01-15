def decodeString(s):
    num = 0
    string = ""
    stack = []
    for c in s:
        if c.isdigit():
            # if the digit before [ is >= 10, num*10
            num = num*10 + int(c)  # num = 3;... ;num = 2
        elif c.isalpha():
            string += c  # ..; a; aaa; bc
        elif c == '[':
            stack.append(string)  # ...; ["aaa"]
            stack.append(num)  # 3; ["aaa", 2]
            string = ""
            num = 0
        elif c == ']':
            pre_num = stack.pop()  #...; 3; 2
            pre_string = stack.pop()  #...; ""; "aaa"
            string = pre_string + pre_num*string  # aaa; aaabcbc
    return string


s = "3[a]2[bc]"
s = "3[a2[c]]"
s = "2[abc]3[cd]ef"
print(decodeString(s))


