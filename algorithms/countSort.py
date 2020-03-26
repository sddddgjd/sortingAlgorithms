def countSort(array, maxValue):
  count = [0 for i in range(0, maxValue + 1)]
  
  for element in array:
    count[element] += 1
  
  for i in range(1, maxValue + 1):
    count[i] += count[i-1]

  sortedArray = [0 for i in range(0, len(array))]

  for element in array:
    sortedArray[ count[element] - 1 ] = element
    count[element] -= 1
  
  return sortedArray

#print(countSort([1,1,2,2,2,5,10], 10))