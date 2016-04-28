def place(k, X):
    i = 0
    while i < k:
        if X[i] == X[k] or abs(X[i] - X[k]) == abs(i - k):
            return False
        i += 1
    return True


# 1-n棋盘
# 0-1棋子
def n_queens(n):
    X = [0 for x in range(n)]  # 棋子都没有放
    k = 0  # 0号棋子

    while k > -1:
        X[k] += 1  # 往右移动一格

        while X[k] <= n and not place(k, X):  # 冲突
            X[k] += 1  # 往右移动一格
        if X[k] <= n:  # 没有越界
            if k == n - 1:
                print(X)
            else:
                k += 1
                X[k] = 0
        else:
            k -= 1


n_queens(4)
