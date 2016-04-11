a = (3, 5, 2, 1, 10)
b = (2, 7, 3, 6, 10)
c = (10, 3, 15, 12, 7, 2)
d = (7, 2, 4, 15, 20, 5)
f = (5, 10, 3, 12, 5, 50, 6)
g = (30, 35, 15, 5, 10, 20, 25)


# --Start by setting m[i,i]=0 for i = 0,…,n-1.
# --Then compute m[0,1], m[1,2],…,m[n-2,n-1].
# --Then m[0,2], m[1,3],…,m[n-3,n-1],…
# --… so on till we can compute m[0,n-1].

def matrix_chain_order(p):
    n = len(p) - 1  # 矩阵数目

    m = [[0 for col in range(n)] for row in range(n)]
    s = [[0 for col in range(n)] for row in range(n)]
    for i in range(0, n - 1):
        m[i][i] = 0

    for l in range(1, n):  # 第一层循环
        for i in range(0, n - l):  # 第二层循环（斜向）i纵坐标
            j = i + l  # j横坐标
            m[i][j] = float("inf")  # 要计算的值，预设为无穷大
            for k in range(i, j):  # 第三层循环 以当前元素所有左边的坐标开始，计算所有可能情况，比较得出最小值
                q = m[i][k] + m[k + 1][j] + p[i] * p[k+1] * p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k + 1

    print_optimal_parens(s, 0, n - 1)
    print()
    return m, s


def print_optimal_parens(s,i,j):
    if i == j:
        print('A%s'%(i+1), end='')
    else:
        print('(', end='')
        print_optimal_parens(s, i, s[i][j]-1)
        print_optimal_parens(s, s[i][j], j)
        print(')', end='')

m, s = matrix_chain_order(g)
print(m)
print(s)



