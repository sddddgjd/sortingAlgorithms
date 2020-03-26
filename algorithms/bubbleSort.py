def bubbleSort(array, *args):
  length = len(array)

  for i in range(length):
    for j in range(0, length - i - 1):
      if array[j] > array[j + 1]: 
        array[j], array[j + 1] = array[j + 1], array[j]
  
  #print (array)
