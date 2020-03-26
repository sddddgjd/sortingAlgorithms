from algorithms.radixSort import radixSort
from algorithms.quickSort import quickSort
from algorithms.mergeSort import mergeSort
from algorithms.bubbleSort import bubbleSort
from algorithms.countSort import countSort
import random
import datetime

tests = [
  {'length': 10, 'maxValue': 100000},
  {'length': 100, 'maxValue': 1000},
  {'length': 1000, 'maxValue': 10000000},
  {'length': 10000, 'maxValue': 1000000},
  {'length': 10000, 'maxValue': 100000}
]

sortingAlgs = [countSort, quickSort, radixSort, mergeSort, bubbleSort]
keys = ['Count sort:', 'Quick sort:', 'Radix sort: ', 'Merge Sort:', 'Bubble Sort:']

for test in tests:
  array = [random.randrange(0, test['maxValue']) for i in range(0, len(test))]
  key = 0
  print(test)
  print('\n')
  for sort in sortingAlgs:
    timeBefore = datetime.datetime.now()
    sort(array, test['maxValue'])
    passed = datetime.datetime.now() - timeBefore

    print(keys[key])
    print(passed)
    print('\n')
    key = key +1
  print('#################')