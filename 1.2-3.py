def smallest_value():
  n = 2

  while True:
    time1 = 100 * (n**2)
    time2 = 2**n

    if time1 < time2:
      break
    n = n + 1

  return n

print smallest_value()