def LIS(A):
    n = len(A)
    F = [1] * n
    P = [[] for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j]:
                if F[i] < F[j] + 1:
                    F[i] = F[j] + 1
                    P[i] = [j]
                elif F[i] == F[j] + 1:
                    P[i].append(j)

    return F, P
#
#
# def printAllLIS(A):
#     i, _, P = LIS(A)
#
#     def recur(i, sub=[]):
#         if not P[i]:
#             print([A[i]] + sub)
#             return 1
#
#         count = 0
#         for j in P[i]:
#             count += recur(j, [A[i]] + sub)
#         return count
#
#     return recur(i)
#
#
# def printAllLIS(A):
#     i, F, P = LIS(A)
#     n = F[i]
#     result = [None] * n
#     total = 0
#
#     def recur(i, k):
#         result[k] = A[i]
#         k -= 1
#         print(A[i])
#         nonlocal total
#         total += 1
#         print('here', total, 'k', k)
#         if not P[i]:
#             print(result)
#             return 1
#
#         count = 0
#         for j in P[i]:
#             count += recur(j, k)
#         return count
#
#     return recur(i, n-1)
#
#
# def printAllLIS(A):
#     F, P = LIS(A)
#
#     L = []
#     n = 0
#     for i in range(len(F)):
#         if F[i] > n:
#             n = F[i]
#             L = [i]
#         elif F[i] == n:
#             L.append(i)
#
#     if n == 1:
#         print(*A, sep='\n')
#         return len(A)
#
#     result = [None] * n
#
#     def recur(i, k):
#         # print('now', i, k)
#         result[k] = A[i]
#         k -= 1
#         if not P[i]:
#             print(*result)
#             return 1
#
#         count = 0
#         for j in P[i]:
#             count += recur(j, k)
#         return count
#
#     count = 0
#     for i in L:
#         # print('running for', i)
#         count += recur(i, n-1)
#
#     return count


# def printAllLIS(A):
#     F, P = LIS(A)
#
#     L = []
#     n = 0
#     for i in range(len(F)):
#         if F[i] > n:
#             n = F[i]
#             L = [i]
#         elif F[i] == n:
#             L.append(i)
#
#     print(L)
#
#     if n == 1:
#         print(*A, sep='\n')
#         return len(A)
#
#     result = [None] * n
#
#     def recur(i, k):
#         result[k] = A[i]
#         k -= 1
#         if not P[i]:
#             print(*result)
#             return 1
#
#         count = 0
#         for j in P[i]:
#             count += recur(j, k)
#         return count
#
#     count = 0
#     for i in L:
#         for j in P[i]:
#             print('Inputting', j)
#             result[n-1] = A[i]
#             count += recur(j, n-2)
#
#     return count


# if __name__ == '__main__':
#     a = [3, 1, 5, 7, 2, 4, 9, 3, 17, 3]
#     import random
#     a = [random.randint(0, 100) for _ in range(random.randint(2, 100))]
#     # a = [93, 53, 18, 10, 20, 25, 32, 2, 34, 91, 32, 57, 3, 8, 3, 30, 64, 81, 91, 29, 69, 29, 26, 69, 22, 91, 42, 49, 57, 7, 51, 87, 7, 79, 77, 38, 31, 66, 73, 45, 6, 55]
#     # a = [0,2,1,4,3,6,5,8,7,10,9,12,11,14,13,16,15,18,17,20,19,22,21,24,23,26,25,28,27,30,29,32,31,34,33,36,35,38,37,40,39,42,41,44,43,46,45,48,47,50,49,52,51,54,53,56,55,58,57,60,59,61]
#     # a = [2,1,4,3]
#     print('Input:', a)
#     print(LIS(a))
#     print(printAllLIS(a))


# from collections import deque
#
#
# def LIS(A):
#     n = len(A)
#     F = [1] * n
#     P = [deque() for _ in range(n)]
#
#     for i in range(n - 1, -1, -1):
#         for j in range(n - 1, i, -1):
#             if A[i] < A[j]:
#                 if F[i] < F[j] + 1:
#                     F[i] = F[j] + 1
#                     P[i] = deque([j])
#                 elif F[i] == F[j] + 1:
#                     P[i].appendleft(j)
#
#     return F, P
#
#
# def printAllLIS(A):
#     F, P = LIS(A)
#
#     L = []
#     n = 0
#     for i in range(len(F)):
#         if F[i] > n:
#             n = F[i]
#             L = [i]
#         elif F[i] == n:
#             L.append(i)
#
#     if n == 1:
#         print(*A, sep='\n')
#         return len(A)
#
#     result = [None] * n
#
#     def recur(i, k):
#         # print('now', i, k)
#         result[k] = i  # Should be A[i] but we test if printed in a right order
#         k += 1
#         if not P[i]:
#             print(*result)
#             return 1
#
#         count = 0
#         for j in P[i]:
#             count += recur(j, k)
#         return count
#
#     count = 0
#     for i in L:
#         # print('running for', i)
#         if P[i]:
#             count += recur(i, 0)
#
#     return count


def LIS(A):
    n = len(A)
    F = [1] * n
    N = [[] for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if A[i] < A[j]:
                if F[i] < F[j] + 1:
                    F[i] = F[j] + 1
                    N[i] = [j]
                elif F[i] == F[j] + 1:
                    N[i].append(j)

    return F, N


def getBeginLIS(F):
    B = []
    n = 0
    for i in range(len(F)):
        if F[i] > n:
            n = F[i]
            B = [i]
        elif F[i] == n:
            B.append(i)
    return B


def printAllLIS(A):
    F, N = LIS(A)
    B = getBeginLIS(F)
    n = F[B[0]]

    if n == 1:
        print(*A, sep='\n')
        return len(A), len(A)

    result = [None] * n

    total_steps = 0

    def recur(i, k):
        nonlocal total_steps
        total_steps += 1
        result[k] = i  # Should be A[i] but we test if printed in a right order
        k += 1
        if not N[i]:
            # print(*result)
            return 1

        count = 0
        for j in range(len(N[i])-1, -1, -1):
            count += recur(N[i][j], k)
        return count

    count = 0
    for i in B:
        count += recur(i, 0)

    return count, total_steps


if __name__ == '__main__':
    # a = [3, 1, 5, 7, 2, 4, 9, 3, 17, 3]
    import random
    from time import time
    while True:
        a = [10 * k + i for k in range(8) for i in range(6, 0, -1)]
        # a = [random.randint(0, 100) for _ in range(random.randint(2, 20))]
        # a = [93, 53, 18, 10, 20, 25, 32, 2, 34, 91, 32, 57, 3, 8, 3, 30, 64, 81, 91, 29, 69, 29, 26, 69, 22, 91, 42, 49, 57, 7, 51, 87, 7, 79, 77, 38, 31, 66, 73, 45, 6, 55]
        # a = [0,2,1,4,3,6,5,8,7,10,9,12,11,14,13,16,15,18,17,20,19,22,21]
        # a = [2, 1, 4, 3]
        print('Input:', a)
        print(LIS(a))
        start = time()
        res, steps = printAllLIS(a)
        end = time()
        print('Result:', res)
        print('Total time:', end - start)

        """
        ATTENTION: 
        A test below is to assess whether an algorithm runs in O(n^2) time.
        We can check that this algorithm (and all possible algorithms) may
        run much slower than O(n^2) when a time required to get/store/print
        all possible increasing subsequences exceeds a time complexity of
        finding the longest one (to see what's going on, run a test below):
        a = [10 * k + i for k in range(8) for i in range(6, 0, -1)]
        """
        n = len(a)
        print('\nInput size (n): ', n)
        print('Max expected sequences steps: (n^2):', n ** 2)
        print('Resulting sequences steps:', steps)
        if steps >= n ** 2:
            print('MORE THAN n^2 OR EQ (see above)')
            break
        break  # DELME IF USING RANDOM
