from random import randint, seed


def mergesort(T):
	if len(T) <= 1: return T

	mid_idx = len(T) // 2
	# Sort recursively a left and a right part of an array
	left = mergesort(T[:mid_idx])
	right = mergesort(T[mid_idx:])

	# Return a merged array
	return merge(left, right)


def merge(left, right):
	merged = []
	left_idx = right_idx = 0

	# Rewrite values in a right (non-descending) order
	while left_idx < len(left) and right_idx < len(right):
		if left[left_idx] < right[right_idx]:
			merged.append(left[left_idx])
			left_idx += 1
		else:
			merged.append(right[right_idx])
			right_idx += 1

	# Rewrite remaining values if there are some in one of the parts
	for i in range(left_idx, len(left)):
		merged.append(left[i])

	for i in range(right_idx, len(right)):
		merged.append(right[i])

	return merged


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
	if T[i] > T[i+1]:
		print("Błąd sortowania!")
		exit()

print("OK")
