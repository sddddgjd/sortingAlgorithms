# radix sort with bitwise operations

def radixSort(array, *args):
  placeholderArray = [0 for i in range(0, len(array))]

  for shiftAmount in range(0,32, 8):
    count = [0 for i in range(0,256)]

    for element in array:
        count[(element >> shiftAmount) & 255] += 1
    
    for index in range(1,256):
        count[index] += count[index-1]
    
    for element in reversed(array):
      index = (element >> shiftAmount) & 255
      placeholderArray[count[index] - 1] = element
      count[index] -= 1
    
    array = placeholderArray
  
  return array

#print(radixSort([1,5,200,90,10]))