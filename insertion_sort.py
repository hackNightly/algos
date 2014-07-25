import time
import random

def insertion_sort():
  start = time.clock()

  arr = [random.randint(0,30) for r in range(10)]

  for j in range(1, len(arr)):
    key = arr[j]
    i = j - 1

    while i >= 0 and arr[i] > key:
      arr[i + 1] = arr[i]
      i = i - 1

    arr[i + 1] = key

  total = time.clock() - start / 1000

  print "insertion sort took {0} seconds for {1} elements".format(total, len(arr))
  print arr


insertion_sort()

