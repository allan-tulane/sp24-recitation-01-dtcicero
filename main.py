"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
import sys
###



def linear_search(mylist, key):
  """ done. """
  for i, v in enumerate(mylist):
    if v == key:
      return i
  return -1


def binary_search(mylist, key):
  """ done. """
  return _binary_search(mylist, key, 0, len(mylist) - 1)


def _binary_search(mylist, key, left, right):
  if left <= right:
    mid = left + (right - left) // 2

    if mylist[mid] == key:
      return mid
    elif mylist[mid] < key:
      return _binary_search(mylist, key, mid + 1, right)
    else:  # mylist[mid] > key
      return _binary_search(mylist, key, left, mid - 1)
  else:
    return -1


def time_search(search_fn, mylist, key):

  start_time = time.time()
  search_fn(mylist, key)
  end_time = time.time()

  elapsed_time_ms = (end_time - start_time) * 1000
  return elapsed_time_ms

###


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):

  results = []

  for n in sizes:

    mylist = list(range(int(n)))

    linear_search_time = time_search(linear_search, mylist, -1)

    binary_search_time = time_search(binary_search, mylist, -1)

    results.append((int(n), linear_search_time, binary_search_time))

  return results


def print_results(results):
  """ done """
  print(
      tabulate.tabulate(results,
                        headers=['n', 'linear', 'binary'],
                        floatfmt=".3f",
                        tablefmt="github"))





print_results(compare_search())