import csv
import random


arrays = [['length', 'random', 'sorted', 'reversed']]


def add_array_range(x, y, size):
    for i in range(size):
        length = random.randint(x, y)
        array = []
        for j in range(length):
            array.append(random.randint(1, 1000000))
            sorted_array = sorted(array)
            reversed_array = reversed(array)
        arrays.append([length, array, sorted_array, list(reversed_array)])


add_array_range(10, 100, 10)
add_array_range(100, 10000, 50)
add_array_range(10000, 20000, 5)


with open('arrays.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(arrays)
