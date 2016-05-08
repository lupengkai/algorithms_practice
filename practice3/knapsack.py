def knapsack_0_1(v, w, n, W):
    # v, value 数组
    # w, weight数组
    # n, 数量
    # W, 最大重量
    c = [[0 for col in range(n + 1)] for row in range(W + 1)]
    for x in range(W + 1):
        c[0][x] = 0
    for i in range(n - 1):
        c[i][0] = 0
        for x in range(1, W - 1):
            if w[i] < W:
                if v[i] + c[i - 1, x - w[i]] > c[i - 1, x]:
                    c[i, x] = v + c[i - 1, x - w[i]]
                else:
                    c[i, x] = c[i - 1, x]
            else:
                c[i, x] = c[i - 1, x]


def knapsack_fractional(p, w, W, n):
    x = [0 for x in range(n)]
    c = W  # remaining capacity

    for i in range(0, n):
        if w(i) <= c:
            x[i] = 1
            c = c - w[i]
        else:
            break
    if i <= n:
        x[i] = c / w[i]
    return x
