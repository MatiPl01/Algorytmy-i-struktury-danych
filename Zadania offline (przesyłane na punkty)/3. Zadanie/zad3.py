"""
Funkcja linearselect zwraca wartość, która znalazłaby się na k indeksie posortowanej
tablicy A.

Funkcja ta wykorzystuje funkcję median_of_medians do efektywnego wyznaczenia
przybliżonej mediany wartości obecnie sprawdzanej części tablicy (od indeksu left_idx
do indeksu right_idx), korzystając z algorytmu zwanego Magicznymi Piątkami (nie jest
konieczne korzystanie z magicznych piątek, ponieważ funkcja umożliwia wskazanie własnej
liczby elementów (jako parametr k), z których ma być wyznaczana mediana).

W kolejnym kroku, funkcja _partition, wykorzystując wyznaczoną wcześniej medianę median
jako pivot, dzieli obecnie przeszukiwaną część tablicy na 2 fragmenty. W pierwszym
fragmencie znajdą się wyłącznie wartości mniejsze od pivota, a w drugim większe lub
równe pivotowi. Funkcja zwraca funalną pozycję pivota.

Ostatnim krokiem jest sprawdzenie, czy indeks, na którym umieszczony został pivot,
jest równy indeksowi, dla którego wartość należy wyznaczyć. Jeżeli nie, konieczne
jest przeszukanie odpowiedniego fragmentu tablicy, na które została ona podzielona,
po wywołaniu funkcji _partition.

Algorytm działa w miejscu i akceptuje wielokrotne wystąpienia tej samej wartości.
"""
from random import randint, shuffle, seed


def linearselect(A, k):
    if not 0 <= k < len(A):
        raise IndexError(f'array index too {"small" if k < 0 else "large"}')
    if len(A) == 1:
        return A[0]

    # Prepare variables which indicate the bounds of the subarray searched
    left_idx = 0
    right_idx = len(A) - 1

    # Loop till the subarray is not empty
    while left_idx <= right_idx:
        # Calculate a median of medians and store this value on the left_idx
        median_of_medians(A, left_idx, right_idx)
        # Partition the current subarray using a median calculated above
        # as a pivot value
        pivot_idx = _partition(A, left_idx, right_idx)

        # If a pivot was placed before the index desired, we have to look for
        # a desired value int the right part of the current subarray
        if pivot_idx < k:
            left_idx = pivot_idx + 1
        # If a pivot was placed after the index desired, we have to search
        # for a value in the left part of the current subarray
        elif pivot_idx > k:
            right_idx = pivot_idx - 1
        # Otherwise, (if k == pivot_idx) return a value which was searched
        else:
            return A[k]


def median_of_medians(arr: list, left_idx: int, right_idx: int, k: int = 5) -> 'median of medians':
    """
    A function which moves a median of medians of k-element subarrays
    to the left_idx of an array passed.
    """
    # Store the position on which the next median will be stored
    # (we will store each median of current k-element subarrays one
    # after another at the beginning of the subarray which begins
    # on the left_index and ends on the right_idx (inclusive)
    next_swap_idx = left_idx

    # Loop till the current subarray has more than k elements
    while right_idx - left_idx >= k:
        # Calculate and store a median of each full k-element subarray
        for end_idx in range(left_idx + k-1, right_idx + 1, k):
            # Store a median on the next index just after the last median stored
            # (swap a median with a value placed after previously calculated medians)
            _swap(arr, next_swap_idx, _select_median(arr, end_idx - k + 1, end_idx))
            next_swap_idx += 1

        # Calculate and store a median of the remaining subarray
        # (which has less than k elements)
        if end_idx < right_idx - 1:
            _swap(arr, next_swap_idx, _select_median(arr, end_idx, right_idx))
            next_swap_idx += 1

        # Prepare variables for the next loop (we will calculate a median of
        # the subarray of medians calculated above, so the right_idx will now
        # be equal to the index of the last median previously determined)
        right_idx = next_swap_idx - 1
        next_swap_idx = left_idx

    # Finally, swap a median of the subarray of medians (which has no more than
    # k elements) with the first (leftmost) value of the subarray
    _swap(arr, left_idx, _select_median(arr, left_idx, right_idx))
    # Return a value of a median
    return arr[left_idx]


def _select_median(arr: list, left_idx: int, right_idx: int) -> int:
    """
    A function which sorts a part of a subarray delimited by
    the left_idx and the right_idx and returns an index of a median.
    """
    # Using the Selection Sort concept, sort only elements of the
    # subarray which are placed up to the middle index (including
    # the middle element)
    mid_idx = (right_idx + left_idx) // 2
    for i in range(left_idx, mid_idx + 1):
        min_idx = i
        for j in range(i + 1, right_idx + 1):
            if arr[j] < arr[min_idx]:
                min_idx = j
        _swap(arr, min_idx, i)
    # Return the middle index which is a position of the median
    # after sorting a part of the subarray
    return mid_idx


def _swap(arr: list, i: int, j: int):
    """
    A helper function which swaps elements of an array
    """
    arr[i], arr[j] = arr[j], arr[i]


def _partition(arr: list, left_idx: int, right_idx: int) -> int:
    """
    A function which partitions a subarray (part of the input array from the
    left_idx to the right_idx) into elements greater than or equal to the pivot
    element (the leftmost value of a subarray) and lower than a pivot.
    This function returns a final position of the pivot value in the sorted array
    (a position on which a pivot will be placed after sorting the input array).
    """
    # After running the median of medians function a pivot (this median of medians)
    # will be placed on the left_idx of the subarray
    pivot = arr[left_idx]

    # Partition an array into 2 subarrays: the first one of elements lower than
    # a pivot and the second one of elements greater than or equal to a pivot
    i = left_idx + 1
    for j in range(left_idx, right_idx + 1):
        if arr[j] < pivot:
            _swap(arr, i, j)
            i += 1

    # Place a pivot element on its destination index
    _swap(arr, i - 1, left_idx)

    return i - 1  # Return a pivot position after the last swap


seed(42)

n = 11
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")
