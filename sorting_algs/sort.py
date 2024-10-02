def bubble_sort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def selection_sort(a):
    for i in range(len(a)):
        min_i = i
        for j in range(i + 1, len(a)):
            if a[j] < a[i]:
                min_i = j
        if j != i:
            a[min_i], a[i] = a[i], a[min_i]

    return a


def insertion_sort(a):
    for i in range(1, len(a)):
        cur = a[i]
        j = i - 1

        while j >= 0 and cur < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = cur
    return a
