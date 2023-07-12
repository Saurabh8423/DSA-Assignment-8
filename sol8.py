def canBeEqual(s, goal):
    if len(s) != len(goal):
        return False

    mismatch = []
    s_diff = []

    for i in range(len(s)):
        if s[i] != goal[i]:
            mismatch.append(i)
        s_diff.append(s[i])

    if len(mismatch) != 2:
        return False

    return (
        s[mismatch[0]] == goal[mismatch[1]] and s[mismatch[1]] == goal[mismatch[0]]
    ) or (
        s_diff[mismatch[0]] == goal[mismatch[1]] and s_diff[mismatch[1]] == goal[mismatch[0]]
    )
s = "ab"
goal = "ba"
print(canBeEqual(s, goal))  # Output: True
