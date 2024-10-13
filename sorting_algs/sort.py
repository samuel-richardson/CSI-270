def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min_i = i
        for j in range(i + 1, n):
            if a[j] < a[min_i]:
                min_i = j
        if j != i:
            a[min_i], a[i] = a[i], a[min_i]

    return a


def insertion_sort(a):
    for i in range(1, len(a)):
        cur = a[i]
        index = i

        for j in range(i-1, -1, -1):
            if a[j] > cur:
                a[j+1] = a[j]
                index = j
            else:
                break
        a[index] = cur
    return a
