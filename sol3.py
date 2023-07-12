def minStepsToEqual(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] + 1

    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] + 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1)

    return dp[m][n]
word1 = "sea"
word2 = "eat"
print(minStepsToEqual(word1, word2))  # Output: 2
