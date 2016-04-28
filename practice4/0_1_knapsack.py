# use back tracking DFS





def bound(p, w, k, M, W, P, n):
    b = p
    c = w
    for i in range(k + 1, n):
        c = c + W[i]
        if c < M:
            b = b + P[i]
        else:
            return (b + (1 - (c - M) / W[i]) * P[i])
    return b


def knapsack(M, n, W, P):
    cw = 0  # 当前
    cp = 0
    k = 0
    fp = -1
    X = [0 for x in range(n)]
    Y = [0 for x in range(n)]

    while True:
        # 先走左子树
        while k <= n - 1 and cw + W[k] <= M:
            cw = cw + W[k]
            cp = cp + P[k]
            Y[k] = 1
            k += 1

        # 目前最大，如果第一次找到的答案就是最大的，后面不会走出去
        if k > n - 1:
            fp = cp
            fw = cw
            k = n - 1
            X = Y
            print(X)
        else:
            Y[k] = 0
        # 往下走没有希望比最大还大
        while bound(cp, cw, k, M, W, P, n) <= fp:
            while k != -1 and Y[k] != 1:  # 左子树走过不用再走
                k -= 1  # 往回走
            if k == -1:
                print(fp)
                return

            # 换条路
            Y[k] = 0
            cw = cw - W[k]
            cp = cp - P[k]
        k += 1


W = [30, 10, 20, 50, 40]
P = [65, 20, 30, 60, 40]
knapsack(100, 5, W, P)
