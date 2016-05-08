def merge(A, B, n):
    i = 0
    j = 0
    k = 0
    C = [0 for _ in range(n)]
    while k < n:
        if A[i] > B[j]:
            C[k] = A[i]
            k += 1
            i += 1
        else:
            C[k] = B[j]
            k += 1
            j += 1
