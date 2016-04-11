a = {'X': 'xzyzzyx', 'Y': 'zxyyzxz'}

d = {'X': 'MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCALLAAQANKESSSESFISRLLAIVAD',
     'Y': 'MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCTLLAAQANKENSNESFISRLLAIVAG'}
X = 'abcbdab'
Y = 'bdcaba'


def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for col in range(n + 1)] for row in range(m + 1)]  # m+1 行 n+1 列
    b = [[0 for col in range(n + 1)] for row in range(m + 1)]
    for i in range(1, m + 1):
        c[i][0] = 0
    for j in range(0, n + 1):
        c[0][j] = 0

    for i in range(1, m + 1):  # 纵向
        for j in range(1, n + 1):  # 横向
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1  # 左上数值加1
                b[i][j] = 3
            elif c[i - 1][j] >= c[i][j - 1]:  # 上边大于等于左边
                c[i][j] = c[i - 1][j]  # 上边的值
                b[i][j] = 2
            else:
                c[i][j] = c[i][j - 1]  # 左边的值
                b[i][j] = 1

    print_LCS(b, x, m, n)
    print()

    return c, b


def print_LCS(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == 3:
        print_LCS(b, X, i - 1, j - 1)  # 两个都去掉最后的字母 往左上
        print(X[i - 1], end='')
    elif b[i][j] == 2:
        print_LCS(b, X, i - 1, j)  # X去掉最后一个字母 往上
    else:
        print_LCS(b, X, i, j - 1)  # Y去掉最后一个字母 往左


c, b = lcs_length(a['X'], a['Y'])
print(c)
print(b)

print()

c, b = lcs_length(d['X'], d['Y'])
print(c)
print(b)
