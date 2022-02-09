"""
O(n)

x ∈ [0, 1] - rozkład jednostajny
Ponieważ dostajemy liczby postaci a^x, nasz zakres wartości dla x ∈ [0, 1]
wynosi [a^0, a^1] = [1, a]
Musimy więc jakoś przemapować te liczby na liczby o rozkładzie jednostajnym.
Przyjmijmy więc, że y = a^x (każda z liczb, jakie otrzymujemy do posortowania,
jest tej postaci). W takiej sytuacji, możemy obustronnie zlogarytmować równanie
i otrzymujemy:
log_a(y) = log_a(a^x)
log_a(y) = x
Zatem liczby postaci log_a(y) są z rozkładu jednostajnego na przedziale [0, 1],
bo x jest z rozkładu jednostajnego na tym przedziale. Wystarczy więc posortować
tablicę liczb y po wartościach log_a(y), przy pomocy algorytmu Bucket Sort (tylko
ten się nadaje, bo Counting Sort oraz Radix Sort nie radzą sobie z liczbami
zmiennoprzecinkowymi). Ważna uwaga, musimy stworzyć liczbę wiaderek zależną od
wielkości wejścia. Ja przyjąłem, że jeżeli w tablicy są nie więcej niż 24 liczby,
od razu sortujemy Insertion Sortem w czasie stałym (bo mamy maksymalnie 24 elementy),
a jeżeli ta liczba jest większa od 24, zmniejszam próg do 2 / 3 * 24 = 16 i dzielę
n liczb na z tablicy wyjściowej na n/16 wiaderek, a następnie, dla każdego wiaderka,
jeżeli liczba elementów w nim nie przekracza 24, sortuję je Insertion Sortem, a
jeżeli wciąż przekracza tę liczbę, to znów Bucket Sortem.
"""

from zad3testy import runtests
import math


# Use k as a threshold which indicates when to start using Insertion Sort
def bucket_sort(arr, *, k: 'threshold' = 24):
    # If a bucket is small enough, use an Insertion Sort algorithm to
    # sort this bucket
    if len(arr) <= k:
        insertion_sort(arr)
    else:
        _bucket_sort(arr, k)


def _bucket_sort(arr, k):
    # Store the maximum and the minimum value of a bucket
    min_val, max_val = minmax(arr)
    # Sort a bucket if only there is more than one unique value
    if min_val != max_val:
        # Make a threshold a bit smaller as a number of elements in each
        # bucket can slightly vary and we don't want to make unnecessary
        # recursive calls.
        m = int(2 / 3 * k)
        # Create buckets
        buckets_count = len(arr) // m + 1
        buckets = [[] for _ in range(buckets_count)]
        val_interval = (max_val - min_val) / buckets_count
        # Distribute values to the proper buckets
        for val in arr:
            # Calculate the bucket's index depending on how much the
            # current value is greater than the lowest one
            bucket_idx = int((val - min_val) / val_interval - .5)
            buckets[bucket_idx].append(val)
        # Sort each bucket separately
        for bucket in buckets:
            # Bucket sort all of the buckets again
            bucket_sort(bucket, k=k)
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


def fast_sort(tab, a):
    n = len(tab)
    for i in range(n): tab[i] = (math.log(tab[i], a), tab[i])
    bucket_sort(tab)
    for i in range(n): tab[i] = tab[i][1]
    return tab


runtests(fast_sort)
