# Write a function that takes in a Binary Tree and returns a list of its branch sums 
# (ordered from leftmost branch sum to rightmost branch sum). A branch sum is the sum of 
# all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts 
# at the root node and ends at any leaf node. Each Binary Tree node has a value stored in a property 
# called "value" and two children nodes stored in properties called "left" and "right," respectively. 
# Children nodes can either be Binary Tree nodes themselves or the None (null) value.

# time = O(N) // we have to traverse all the node to account for each value, we are only doing constant time expressions
# space = O(log(N))  effective by the list of the branch sum and also by the recursive nature of the solution, we have multiple recursive function calls at once.

class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
def branchSum(root):
  sums = []
  calculateBranchSums[root, 0, sums]
  return sums
  
def calculateBranchSum[node, runningSum, sum]:
  
  
