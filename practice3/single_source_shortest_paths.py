INF = 65535


def bellman_ford(n, w, s, E):
    d = [INF for _ in range(n)]
    d[s] = 0

    for i in range(n - 1):
        for (u, v) in E:
            if d[v] > d[u] + w[u][v]:
                d[v] = d[u] + w[u][v]
    for (u, v) in E:
        if d[v] > d[u] + w[u][v]:
            print('a negative-weight cycle exists.')
            return
    print(d)


n = 5
w = [[INF for col in range(n)] for row in range(n)]
w[0][1] = -1
w[0][2] = 3
w[1][2] = 3
w[1][3] = 2
w[1][4] = 2
w[3][1] = 1
w[3][2] = 5
w[4][4] = -3

E = [(0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (3, 1), (3, 2), (4, 4)]
s = 0

bellman_ford(n, w, s, E)
