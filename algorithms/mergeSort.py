def merge(left, right):
  
	i,j = 0,0
	mergedList = []

	while i<len(left) and j<len(right):

		if left[i] <= right[j]:
			mergedList.append(left[i])
			i += 1
		else:
			mergedList.append(right[j])
			j += 1

  # append remaining elements if there are any
	mergedList += left[i:]
	mergedList += right[j:]

	return mergedList

def mergeSort(array, *args):

	if len(array) <= 1:
		return array
	else:
		middle = int(len(array)/2)

		left = mergeSort(array[:middle])
		right = mergeSort(array[middle:])

		return merge(left, right)

#print(sort([5, 10, -5, 1000, 20]))