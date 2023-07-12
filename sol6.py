def findAnagrams(s, p):
    result = []
    freqP = [0] * 26
    freqWindow = [0] * 26

    for char in p:
        freqP[ord(char) - ord('a')] += 1

    left = right = 0
    while right < len(s):
        freqWindow[ord(s[right]) - ord('a')] += 1

        if right - left + 1 == len(p):
            if freqP == freqWindow:
                result.append(left)

            freqWindow[ord(s[left]) - ord('a')] -= 1
            left += 1

        right += 1

    return result
s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))  # Output: [0, 6]

