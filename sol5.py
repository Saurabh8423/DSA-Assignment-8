def compress(chars):
    readPtr = 0
    writePtr = 0
    count = 1

    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]:
            count += 1
        else:
            chars[writePtr] = chars[readPtr]
            writePtr += 1
            if count > 1:
                countStr = str(count)
                for digit in countStr:
                    chars[writePtr] = digit
                    writePtr += 1
            count = 1
            readPtr = i

    chars[writePtr] = chars[readPtr]
    writePtr += 1
    if count > 1:
        countStr = str(count)
        for digit in countStr:
            chars[writePtr] = digit
            writePtr += 1

    return writePtr
chars = ["a","a","b","b","c","c","c"]
newLength = compress(chars)
print(newLength)  # Output: 6
print(chars[:newLength])  # Output: ["a", "2", "b", "2", "c", "3"]

