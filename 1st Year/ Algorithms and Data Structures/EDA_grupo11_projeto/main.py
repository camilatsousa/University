import time
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.use('TkAgg')


def partitions(file_name, partition_size):
    file_name = pd.read_csv(file_name)
    file_name = file_name.iloc[:, 0].tolist()
    if partition_size == 0:
        raise ValueError("Number invalid")
    num_partitions = len(file_name) // partition_size + (len(file_name) % partition_size > 0)
    partitions = (file_name[i * partition_size:(i + 1) * partition_size] for i in range(num_partitions))
    for partition in partitions:
        yield partition


def partition2(lst, ini, end):
    i = ini - 1
    pivot = lst[end]
    for j in range(ini, end):
        if lst[j] <= pivot:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[end] = lst[end], lst[i + 1]
    return i + 1


def quicksort(lst, ini, end, num_iterations):
    if ini < end:
        if num_iterations > 0:
            partir = partition2(lst, ini, end)
            num_iterations = num_iterations - 1
            quicksort(lst, ini, partir - 1, num_iterations)
            quicksort(lst, partir + 1, end, num_iterations)
        else:
            lst[ini:end + 1] = sorted(lst[ini:end + 1])


def sorting(lst, is_quicksort, num_iterations):
    partition = lst.copy()
    if is_quicksort:
        quicksort(partition, 0, len(partition) - 1, num_iterations)
    else:
        partition.sort()
    return partition


def execute(data, n, ascending):
    results = []
    for partition in partitions(data, n):
        start_time = time.time()
        sorting(partition, True, 2)
        duration = time.time() - start_time
        if ascending:
            max_val, min_val = max(partition), min(partition)
        else:
            max_val, min_val = min(partition), max(partition)
        num_iterations = len(partition) // 2
        results.append((duration, max_val, min_val, num_iterations))

    df = {
        'duration': [r[0] for r in results],
        'max_val': [r[1] for r in results],
        'min_val': [r[2] for r in results],
        'num_iterations': [r[3] for r in results],
    }

    df = pd.DataFrame(df)
    print(df)
    return results


file_name = 'data.csv'
partition_size = 20
for i, partition in enumerate(partitions(file_name, partition_size)):
    sorted_partition = sorting(partition, True, 2)
    print("Partition {}:".format(i + 1))
    print(sorted_partition)

# test
n_values = list(range(1, 100000, 20000))
execution_times = []
for n in n_values:
    for i, partition in enumerate(partitions(file_name, partition_size)):
        sorted_partition = sorting(partition, True, 2)
    results = execute(file_name, n, True)
    total_time = sum([duration for duration, _, _, _ in results])
    execution_times.append(total_time)

plt.plot(n_values, execution_times)
plt.xlabel('Number of observations per partition')
plt.ylabel('Execution time (s)')
plt.show()
