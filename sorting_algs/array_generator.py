import csv
import random


arrays = [['type', 'length', 'array']]


def add_array_range(x, y, size):
    for i in range(size):
        length = random.randint(x, y)
        array = []
        for j in range(length):
            array.append(random.randint(1, 10000))
            sorted_array = sorted(array)
            reversed_array = reversed(array)
        arrays.append(['random', length, array])
        arrays.append(['sorted', length, sorted_array])
        arrays.append(['reversed', length, list(reversed_array)])


add_array_range(10, 100, 5)
add_array_range(1000, 1000, 5)
add_array_range(10000, 10000, 5)


with open('arrays.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(arrays)
