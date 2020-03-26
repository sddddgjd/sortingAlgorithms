# choose median of three
def median(array, left, right):
  if (right - left + 1 < 3):
    return array[left]

  leftValue = array[left]
  midValue = array[(left + right) / 2]
  rightValue = array[right]

  if (rightValue > leftValue):
    leftValue, rightValue = rightValue,leftValue

  if (midValue < leftValue):
    leftValue, midValue = midValue,rightValue

  if (rightValue < midValue):
    midValue, rightValue = rightValue, midValue

  return midValue


def sort(array, left, right):

  pivot = median(array, left, right)

  i = left
  j = right
  while i <= j:

    while array[i] < pivot:
      i += 1
    while array[j] > pivot:
      j -= 1

    if i<=j:
      array[i], array[j] = array[j], array[i]
      i += 1
      j -= 1

  if i < right:
    sort(array, i, right)

  if left < j:
    sort(array, left, j)

def quickSort(array, *args):
  sort(array, 0, len(array) - 1)
  #print(array)
