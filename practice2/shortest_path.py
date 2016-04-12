inf = 65535

G = (
    (inf, 5, 3, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf),
    (5, inf, inf, 1, 3, 6, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf),
    (3, inf, inf, inf, 8, 7, 6, inf, inf, inf, inf, inf, inf, inf, inf, inf),
    (inf, 1, inf, inf, inf, inf, inf, 6, 8, inf, inf, inf, inf, inf, inf, inf),
    (inf, 3, 8, inf, inf, inf, inf, 3, 5, inf, inf, inf, inf, inf, inf, inf),
    (inf, 6, 7, inf, inf, inf, inf, inf, 3, 3, inf, inf, inf, inf, inf, inf),
    (inf, inf, 6, inf, inf, inf, inf, inf, 8, 4, inf, inf, inf, inf, inf, inf),
    (inf, inf, inf, 6, 3, inf, inf, inf, inf, inf, 2, 2, inf, inf, inf, inf),
    (inf, inf, inf, 8, 5, 3, 8, inf, inf, inf, inf, 1, 2, inf, inf, inf),
    (inf, inf, inf, inf, inf, 3, 4, inf, inf, inf, inf, 3, 3, inf, inf, inf),
    (inf, inf, inf, inf, inf, inf, inf, 2, inf, inf, inf, inf, inf, 3, 5, inf),
    (inf, inf, inf, inf, inf, inf, inf, 2, 1, 3, inf, inf, inf, 5, 2, inf),
    (inf, inf, inf, inf, inf, inf, inf, inf, 2, 3, inf, inf, inf, 6, 6, inf),
    (inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 3, 5, 6, inf, inf, 4),
    (inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 5, 2, 6, inf, inf, 3),
    (inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 4, 3, inf)
)


def Dijkstra(G, s):
    n = len(G)  # 矩阵行数
    V1 = {}  # 已加入顶点
    V2 = set(i for i in range(0, n))  # 余下顶点
    path = {}  # 记录到各点的最短路径

    V1[s] = 0
    path[s] = '%s' % s  # 将起始点加入
    V2.remove(s)

    while len(V2) > 0:
        m = 0
        n = 0
        min = inf
        for v in V2:
            for key in V1:
                if G[v][key] < min:
                    min = G[v][key]
                    m = v
                    n = key

        V1[m] = min + V1[n]
        path[m] = path[n] + ' %s' % m
        V2.remove(m)

    print(path)
    print(V1)


Dijkstra(G, 0)
