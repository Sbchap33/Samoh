# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:26:53 2019

@author: dev2
"""
#Test comment from Sam #

## Blahh blahhh number ####

# Finds the smallest value in an array
def findSmallest_LEV(arr):
    
  print("  Finding smallest value in {0}".format(arr))  
    
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  
  print("      **** New smallest values is {0} ****".format(smallest))
  
  for i in range(1, len(arr)):

    print("    Comparing {0} and {1}".format(smallest, arr[i]))
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
      print("      **** New smallest values is {0} ****".format(smallest))
      
      
  print("    DONE searching for smallest value in this iteration which is {0}".format(smallest)) 
  return smallest_index

# Sort array
def selectionSort_LEV(arr):
  newArr = []
  
  print("STARTING SORT ALGORITHM")
  
  for i in range(len(arr)):
      
      # Finds the smallest element in the array and adds it to the new array
      smallest_idx = findSmallest_LEV(arr)
      smallest_val = arr.pop(smallest_idx)
      
      newArr.append(smallest_val)
      
      print("      Smallest value of {0} is at index {1} [---] output array is now {2}".format(smallest_val, smallest_idx, newArr))
      
  print("FINISHING SORT ALGORITHM")    
      
  return newArr

print(selectionSort_LEV([5, 3, 6, 2, 10]))



def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index


def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr


print(selectionSort([5, 3, 6, 2, 10]))





import random
import string
import time

import numpy as np

array_string_5_5000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(5000)]
array_string_5_10000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(10000)]
array_string_5_15000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(15000)]
array_string_5_20000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(20000)]

array_string_15_5000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(5000)]
array_string_15_10000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(10000)]
array_string_15_15000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(15000)]
array_string_15_20000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(20000)]

array_int_5000 = list(np.random.randint(0, 1000000, 5000))
array_int_10000 = list(np.random.randint(0, 1000000, 10000))
array_int_15000 = list(np.random.randint(0, 1000000, 15000))
array_int_20000 = list(np.random.randint(0, 1000000, 20000))

array_float_5000 = list(np.random.random(5000))
array_float_10000 = list(np.random.random(10000))
array_float_15000 = list(np.random.random(15000))
array_float_20000 = list(np.random.random(20000))

start_time = time.time()
out1 = selectionSort(array_string_15_5000)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
out1 = selectionSort(array_string_15_10000)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
out1 = selectionSort(array_string_5_15000)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
out1 = selectionSort(array_string_5_20000)
end_time = time.time()
print(end_time - start_time)



start_time = time.time()
out = selectionSort(array_int_5000)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
out = selectionSort(array_int_10000)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
out = selectionSort(array_int_15000)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
out = selectionSort(array_int_20000)
end_time = time.time()
print(end_time - start_time)



start_time = time.time()
out = selectionSort(array_float_5000)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
out = selectionSort(array_float_10000)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
out = selectionSort(array_float_15000)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
out = selectionSort(array_float_20000)
end_time = time.time()
print(end_time - start_time)



































