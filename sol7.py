def decodeString(s):
    if len(s) == 0:
        return s

    strStack = []
    numStack = []
    res = ""
    idx = 0

    while idx < len(s):
        if s[idx].isdigit():
            num = 0
            while idx < len(s) and s[idx].isdigit():
                num = num * 10 + int(s[idx])
                idx += 1
            numStack.append(num)
        elif s[idx] == '[':
            strStack.append(res)
            res = ""
            idx += 1
        elif s[idx] == ']':
            temp = strStack.pop()
            repeatTimes = numStack.pop()
            for i in range(repeatTimes):
                temp += res
            res = temp
            idx += 1
        else:
            res += s[idx]
            idx += 1

    return res
s = "3[a]2[bc]"
print(decodeString(s))
