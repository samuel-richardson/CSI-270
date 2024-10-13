from sort import bubble_sort, insertion_sort, selection_sort
import csv
import time
import sys

csv.field_size_limit(sys.maxsize)

with open('arrays.csv', newline='') as f:
    reader = csv.reader(f)
    arrays = list(reader)


def test_algs(arrays):
    results = [['Array Length',
                'Bubble Random Execution Time',
                'Bubble Sorted Execution Time',
                'Bubble Reversed Execution Time',
                'Selection Random Execution Time',
                'Selection Sorted Execution Time',
                'Selection Reversed Execution Time',
                'Insertion Random Execution Time',
                'Insertion Sorted Execution Time',
                'Insertion Reversed Execution Time',
                ]]

    def test_time(array, alg):
        start_time = time.time()
        alg(array)
        end_time = time.time()
        return round((end_time - start_time) * 1000, 2)

    for array in arrays[1:]:
        array_length = array[0]
        random_array = [int(a) for a in array[1].strip('[').strip(']').split(', ')]
        sorted_array = [int(a) for a in array[2].strip('[').strip(']').split(', ')]
        reversed_array = [int(a) for a in array[3].strip('[').strip(']').split(', ')]

        results.append([array_length,
                        test_time(random_array, bubble_sort),
                        test_time(sorted_array, bubble_sort),
                        test_time(reversed_array, bubble_sort),
                        test_time(random_array, selection_sort),
                        test_time(sorted_array, selection_sort),
                        test_time(reversed_array, selection_sort),
                        test_time(random_array, insertion_sort),
                        test_time(sorted_array, insertion_sort),
                        test_time(reversed_array, insertion_sort)
                        ])
    with open('results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)


test_algs(arrays)
