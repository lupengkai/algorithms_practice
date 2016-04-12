a = (-2, 11, -4, 13, -5, -2)


def DP_max_sum(a):
    n = len(a)
    sum = 0
    b = 0
    t = [0 for i in range(0, n)]
    q = 0
    p = 0

    for i in range(0, n):  # 以当前字符串结尾的子串
        if b > 0:  # 前面子串和为正，连上
            b += a[i]

        else:
            b = a[i]  # 前面子串和为负，重新开始
            t[i] = 1
        if b > sum:  # 记录下最大的
            sum = b
            q = i
    p = q
    for x in t[:q:-1]:
        p -= 1
        if x == 1:
            break

    return sum, p, q


sum, p, q = DP_max_sum(a)
print('start: ', p)
print('end: ', q)
print(sum)
