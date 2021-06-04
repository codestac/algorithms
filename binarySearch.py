# recursive strategy (with left and right pointer)
# time = O(log(N))
# space = O(log(N))
def binarySearch(array, target):
  #helper method only to return the result of the method
  return binarySearchHelper(array, target, 0, len(array) -1)

def binarySearchHelper(array, target, left, right):
  if left > right:
    return -1
  middle = (left + right) // 2 # rounding the value after dividing
  potentialMatch = array[middle]
  if target == potentialMatch:
    return middle 
  elif target < potentialMatch:
    return binarySearchHelper(array, target, left, middle - 1)
  else:
    return binarySearchHelper(array, target, middle + 1, right)

# iterative strategy
# time = O(log(N))
# space = O(1)
def binarySearch(array, target):
  return binarySearchHelper(array, target, 0, len(array) -1)

def binarySearchHelper(array, target, left, right):
  while left <= rght:
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
      return middle 
    elif target < potentialMatch:
      right = middle - 1
    else:
      left = middle + 1
  return -1
