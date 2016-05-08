INF = 65535


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0 for _ in range(0, n1 + 1)]
    R = [0 for _ in range(0, n2 + 1)]
    for i in range(0, n1 + 1):
        L[i] = A[p + i - 2]
    for j in range(0, n2 + 1):
        R[j] = A[q + j - 1]

    L[n1] = INF
    R[n2] = INF

    i = 0
    j = 0

    for k in range(p - 1, r):
        if L[i - 1] <= R[j - 1]:
            A[k - 1] = L[i - 1]
            i += 1
        else:
            A[k - 1] = R[j - 1]
            j += 1


def binary_sort(A, goal):
    low = 0
    high = len(A) - 1
    while low <= high:
        middle = (high - low) // 2 + low

        if A[middle] == goal:
            return middle;
        elif A[middle] > goal:
            high = middle - 1
        else:
            low = middle + 1
    return -1


def find(A, goal):
    merge_sort(A, 0, len(A) - 1)
    return binary_sort(A, goal)
