def floor(x):
	a = 1
	a = x
	return a

def parent(i):
	if (i % 2 == 0):
		return i/2 - 1
	else:
		return floor(i/2 + 1)

def left(i):
	return 2*i +1

def right(i):
	return 2*i + 2

def max_heapify(arr, i, heap_size):
	#print arr
	l = left(i)
	r = right(i)
	if l <= heap_size and arr[l] > arr[i]:
		largest = l
	else: largest = i
	if r <= heap_size and arr[r] > arr[largest]:
		largest = r
	if (largest != i):
		arr[i] , arr[largest] = arr[largest], arr[i]
		max_heapify(arr, largest, heap_size)

def build_max_heap(arr):
	for i in xrange(len(arr)/2-1, -1, -1):
		max_heapify(arr, i, len(arr)-1)

def heapsort(arr):
	heap_size = len(arr)-1
	build_max_heap(arr)
	#print arr
	heap_size = len(arr)-1
	for i in range(heap_size, 0, -1):
		arr[0], arr[i] = arr[i] , arr[0]
		#print arr[0], arr[i]
		heap_size -= 1
		max_heapify(arr, 0, heap_size)
	print arr


arr = [10,5,567,3,6,2,6,8,34,12,45]
heapsort(arr)