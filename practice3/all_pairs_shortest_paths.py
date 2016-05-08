def Floyd_Warshall(n, c):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if c[i - 1][j - 1] > c[i - 1][k - 1] + c[k - 1][j - 1]:
                    c[i - 1][j - 1] = c[i - 1][k - 1] + c[k - 1][j - 1]
