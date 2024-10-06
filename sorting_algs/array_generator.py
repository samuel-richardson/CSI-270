import csv
import random


arrays = [['length', 'random', 'sorted', 'reversed']]


def add_array_range(x, y, size):
    for i in range(size):
        length = random.randint(x, y)
        array = []
        for j in range(length):
            array.append(random.randint(1, 10000))
            sorted_array = sorted(array)
            reversed_array = reversed(array)
        arrays.append([length, array, sorted_array, list(reversed_array)])


add_array_range(10, 100, 2)
add_array_range(1000, 1000, 2)
add_array_range(10000, 10000, 2)


with open('arrays.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(arrays)
