#!/usr/bin/env python

# fibonacci algorithm
def fibonacci(n):
  if n < 0:
    print('n must be positive.')
  elif n == 0:
    return n
  elif n == 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# find 24th term in fibonacci sequence
fib = fibonacci(24)
print(fib)
# 24th term found to be 46,368
