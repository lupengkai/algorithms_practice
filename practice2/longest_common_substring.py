a = {'X': 'xzyzzyx', 'Y': 'zxyyzxz'}

d = {'X': 'MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCALLAAQANKESSSESFISRLLAIVAD',
     'Y': 'MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCTLLAAQANKENSNESFISRLLAIVAG'}


def lcs_length(x, y):
    p = 0
    q = 0
    max = 0

    m = len(x)
    n = len(y)
    c = [[0 for col in range(n + 1)] for row in range(m + 1)]  # m+1 行 n+1 列

    for i in range(1, m + 1):
        c[i][0] = 0
    for j in range(0, n + 1):
        c[0][j] = 0

    for i in range(1, m + 1):  # 纵向
        for j in range(1, n + 1):  # 横向
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1  # 左上数值加1
                if c[i][j] >= max:
                    max = c[i][j]
                    p = i
                    q = j
    print_LCS(x, p, q, max)
    print()
    return c


def print_LCS(X, i, j, max):
    if max == 0:
        return
    print_LCS(X, i - 1, j - 1, max - 1)  # 两个都去掉最后的字母 往左上
    print(X[i - 1], end='')


c = lcs_length(a['X'], a['Y'])
print(c)

c = lcs_length(d['X'], d['Y'])
print(c)
