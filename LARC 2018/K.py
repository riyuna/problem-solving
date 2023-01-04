from collections import deque


def delete_element(array, element):
	if element >= 0:
		deleted_array = []
		delete_queue = deque([])

		for v in array:
			if delete_queue and delete_queue[0] == v:
				delete_queue.popleft()
			else:
				deleted_array.append(v)
				delete_queue.append(v + element)
		
		if not deleted_array:
			return None
		return deleted_array

	else:
		reversed_array = list(map(lambda x: -x, array[::-1]))
		deleted_array = delete_element(reversed_array, -element)

		if not deleted_array:
			return None

		return list(map(lambda x: -x, deleted_array[::-1]))


def decrypt(array):
	global result
	if array:
		if len(array) == 1:
			return
		
		if array[-1] > 0:
			sign = 1
		else:
			sign = -1

		element = array[-1] - array[-2]
		if element * sign < 0:
			element = -element

		deleted_array = delete_element(array, element)
		if not deleted_array:
			element = array[1] - array[0]
			if element * sign < 0:
				element = -element
			deleted_array = delete_element(array, element)
			result.append(element)
		else:
			result.append(element)

		decrypt(deleted_array)


n = int(input())
result = []
array = [int(input()) for _ in range(2**n)]
decrypt(sorted(array))

print(*sorted(result))
