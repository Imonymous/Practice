#!/usr/bin/env python
import sys
import os
sys.setrecursionlimit(7000)

# TODO: Without the auxillary space

class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None

def bst_insert(root, val):
    if (root == None): # destination.
        return TreeNode(val)
    root_copy = root
    while (1):
        if (val <= root.val and root.left_ptr != None):
            root = root.left_ptr
        elif (val <= root.val):
            root.left_ptr = TreeNode(val)
            return root_copy
        elif (root.right_ptr != None):
            root = root.right_ptr
        else:
            root.right_ptr = TreeNode(val)
            return root_copy
    return root_copy

'''
    For your reference:
    
    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''
def inorder(root, a, k):
    if root == None or len(a) == k:
        return
    
    inorder(root.left_ptr, a, k)
    if len(a) == k:
        return a
    a.append(root)
    if len(a) == k:
        return a
    inorder(root.right_ptr, a, k)
    

def kth_smallest_element(root, k):
    a = []
    inorder(root, a, k)
    return a[-1].val


if __name__ == "__main__":
    f = sys.stdout
    
    N = int(input())

    root = None
    
    for i in range(0, N):
        data = int(input())
        root = bst_insert(root, data)
    k = int(input())
    
    ans = kth_smallest_element(root, k)
    f.write(str(ans) + "\n")

    f.close()
