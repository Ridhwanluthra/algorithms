def merge(arr, p, q, r):
	n1 = q - p
	n2 = r - q
	left = []
	right = []
	for i in xrange(n1):
		left.append(arr[p + i])
	for i in xrange(n2):
		right.append(arr[q + i])
	left.append(float("inf"))
	right.append(float("inf"))
	i = 0
	j = 0
	for k in xrange(p, r + 1):
		#print len(left), len(right)
		#print i, j, k
		try:
			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
		except IndexError:
			print len(left), len(right)
			print i, j
	print arr

def mergesort(arr, p, r):
	if p < r:
		q = 1
		q = (p + r) / 2
		mergesort(arr, p, q)
		mergesort(arr, q + 1, r)
		merge(arr, p, q, r)

arr = [9,8,7,6,5,4,3,2,1,0]
#merge(arr, 0, 5, 9)
mergesort(arr, 0, len(arr)-1)