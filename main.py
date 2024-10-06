import timeit
import random

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Генерація наборів даних
def generate_datasets():
    sizes = [100, 1000, 10000]
    datasets = {
        'random': [random.sample(range(size * 10), size) for size in sizes],
        'sorted': [list(range(size)) for size in sizes],
        'reversed': [list(range(size, 0, -1)) for size in sizes]
    }
    return datasets

# Вимірювання часу виконання
def measure_time():
    datasets = generate_datasets()
    results = {}

    for key, data in datasets.items():
        results[key] = {}
        for arr in data:
            size = len(arr)
            results[key][size] = {}

            # Вимірювання часу для сортування злиттям
            merge_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
            results[key][size]['merge_sort'] = merge_time

            # Вимірювання часу для сортування вставками
            insertion_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
            results[key][size]['insertion_sort'] = insertion_time

            # Вимірювання часу для Timsort (sorted())
            timsort_time = timeit.timeit(lambda: sorted(arr.copy()), number=1)
            results[key][size]['timsort'] = timsort_time

    return results

# Основна функція для запуску аналізу
if __name__ == "__main__":
    results = measure_time()
    for dataset_type, sizes in results.items():
        print(f"Тип набору даних: {dataset_type}")
        for size, times in sizes.items():
            print(f"  Розмір: {size}")
            for sort_type, time_taken in times.items():
                print(f"    {sort_type}: {time_taken:.6f} секунд")