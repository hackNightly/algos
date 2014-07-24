from math import log

def compare_sort():
  n = 2;

  while True:
    merge = 8 * log(n, 2)

    if n > merge:
      break;

    n = n + 1

  return n

print compare_sort()