INF = 100


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) / 2


def max_heapify(A, i):
    l = left(i)
    r = right(i)

    if l <= A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A.heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    for i in [x for x in range(len(A) / 2 + 1)][::-1]:
        max_heapify(A, i)


def heap_extrat_max(A):
    A.heap_size = len(A)
    if A.heap_size < 0:
        raise ValueError('heap underflow')
    max = A[0]
    A[0] = A[A.heap_size]
    max_heapify(A, 0)
    return max


def heap_increase_key(A, i, key):
    if key < A[i]:
        raise ValueError('new key is small than current key')
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def max_heap_insert(A, key):
    A.heap_size += 1
    A[A.heap_size] = -INF
    heap_increase_key(A, A.heap_size, key)
