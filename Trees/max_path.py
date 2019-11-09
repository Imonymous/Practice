#!/usr/bin/env python3

"""
Mock 3

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6


Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

"""

def post_order(root, max_sum):
	if root == None:
		return max_sum, 0

	max_sum, left_path_max = post_order(root.left_ptr, max_sum)
	max_sum, right_path_max = post_order(root.right_ptr, max_sum)

	O1 = [root.val+left_path_max+right_path_max, root.val+left_path_max, root.val+right_path_max, root.val]
	O2 = [root.val+left_path_max, root.val+right_path_max, root.val]

	sub_tree_max_sum = max(O1)

	print(root.val, left_path_max, right_path_max)

	if sub_tree_max_sum > max_sum:
		max_sum = sub_tree_max_sum

	return max_sum, max(O2)


class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

def build_tree(arr, i):
	if i >= len(arr):
		return None

	node = TreeNode()
	if arr[i] is not None:
		node.val = arr[i]
	else:
		node.val = 0
	node.left_ptr = build_tree(arr, 2*i+1)
	node.right_ptr = build_tree(arr, 2*i+2)

	return node

def main(arr):
	root = build_tree(arr, 0)

	max_sum, xyz = post_order(root, 0)

	print(max_sum)

if __name__ == '__main__':
	main([-10,9,20,None,None,15,7,None,None,None,None,3,-2,1,10])
