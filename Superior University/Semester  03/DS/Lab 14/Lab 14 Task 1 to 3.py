# Task 1: Implementing the Fibonacci Sequence Using DP (Memoization & 
# Tabulation) 
# Objective: Understand Dynamic Programming by implementing the Fibonacci sequence 
# using both memoization (top-down) and tabulation (bottom-up) approaches.


def fib_memoization(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]
print(fib_memoization(10))  
def fib_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(fib_tabulation(10))


# Task 2: Implementing the Longest Common Subsequence (LCS) Algorithm 
# Objective: Learn string processing with Dynamic Programming by implementing LCS, 
# which finds the longest subsequence common to two given strings. 




def lcs_memo(s1, s2):
    memo = {}

    def dp(i, j):
        if i == len(s1) or j == len(s2):
            return ""
        if (i, j) in memo:
            return memo[(i, j)]

        if s1[i] == s2[j]:
            memo[(i, j)] = s1[i] + dp(i + 1, j + 1)
        else:
            subseq1 = dp(i + 1, j)
            subseq2 = dp(i, j + 1)
            memo[(i, j)] = subseq1 if len(subseq1) > len(subseq2) else subseq2

        return memo[(i, j)]

    return dp(0, 0)
print(lcs_memo("AGGTAB", "GXTXAYB"))  

def lcs_tabulation(s1, s2):
    m, n = len(s1), len(s2)
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = s1[i] + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1], key=len)

    return dp[0][0]


print(lcs_tabulation("AGGTAB", "GXTXAYB")) 

# Task 3: Implementing the 0/1 Knapsack Problem Using Dynamic 
# Programming 
# Objective: Learn how DP solves optimization problems by implementing the 0/1 
# Knapsack Problem, where you maximize the total value of items without exceeding a given 
# weight limit.


def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], 
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]  
                )
            else:
                dp[i][w] = dp[i - 1][w] 

    return dp[n][capacity]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack(weights, values, capacity)) 


