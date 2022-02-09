from zad1testy import runtests


def combo_sort(arr, *, k: 'threshold' = 24):
    if len(arr) <= k:
        insertion_sort(arr)
    else:
        # Create buckets
        m = int(2 / 3 * k)
        buckets_count = len(arr) // m + 1
        buckets = [[] for _ in range(buckets_count)]
        min_val, max_val = minmax(arr)
        val_interval = (max_val - min_val) / buckets_count
        # Distribute values to the proper buckets
        for val in arr:
            # Calculate the bucket's index depending on how much the
            # current value is greater than the lowest one
            bucket_idx = int((val - min_val) / val_interval - .5)  # Round down in order not to overflow an array
            buckets[bucket_idx].append(val)
        # Sort each bucket separately
        for i in range(len(buckets)):
            if len(buckets[i]) < k:
                insertion_sort(buckets[i])
            else:
                quick_sort(buckets[i])
        # Rewrite sorted values from buckets to the initial array
        i = 0
        for bucket in buckets:
            for val in bucket:
                arr[i] = val
                i += 1


def minmax(arr):
    global_min = global_max = arr[-1]

    for i in range(0, len(arr) - 1, 2):
        if arr[i] > arr[i + 1]:
            if arr[i] > global_max:   global_max = arr[i]
            if arr[i + 1] < global_min: global_min = arr[i + 1]
        else:
            if arr[i + 1] > global_max: global_max = arr[i + 1]
            if arr[i] < global_min:   global_min = arr[i]
    return global_min, global_max


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp


def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, left_idx, right_idx):
    while left_idx < right_idx:
        pivot_position = _partition(arr, left_idx, right_idx)

        if pivot_position - left_idx < right_idx - pivot_position:
            _quick_sort(arr, left_idx, pivot_position)
            left_idx = pivot_position + 1  # I removed a tailing recursion
        else:
            _quick_sort(arr, pivot_position + 1, right_idx)
            right_idx = pivot_position  # I removed a tailing recursion


def _partition(arr, left_idx, right_idx):
    pivot = arr[left_idx]

    # Partition an array into 2 subarrays of elements lower than or
    # equal to a pivot and of elements greater or equal to a pivot
    # (in this partition algorithm pivot isn't placed on a fixed position
    # but can be also swapped like all the remaining values)
    i = left_idx - 1
    j = right_idx + 1
    while True:
        i += 1
        while arr[i] < pivot: i += 1

        j -= 1
        while arr[j] > pivot: j -= 1

        if i < j:
            _swap(arr, i, j)
        else:
            return j  # Return a pivot position after the last swap


def _swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def chaos_index(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    combo_sort(T)

    k = 0
    for i in range(n):
        k = max(k, abs(i - T[i][1]))

    for i in range(n):
        T[i] = T[i][0]

    return k


runtests(chaos_index)
