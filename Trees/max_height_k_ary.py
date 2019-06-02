#!/usr/bin/env python

import sys
import os

sys.setrecursionlimit(101000)

class TreeNode:
    def __init__(self):
        # To find height of tree, value stored in nodes does not matter. So in input also we are not given this field. 
        # self.val = 0
        self.children = []

'''
    For your reference:
    
    class TreeNode:
        def __init__(self):
            self.children = []

'''

def find_height(root):
	if len(root.children) == 0:
		return 0

	height = 0
	for i in range(0, len(root.children)):
		height = max(height, find_height(root.children[i]))

	print(height+1)
	return height+1

address = {}

def build_tree(frm, to):
    N = len(frm) + 1
    address = {}
    for i in range(1, N + 1):
        address[i] = TreeNode()
    for i in range(0, N - 1):
        address[frm[i]].children.append(address[to[i]])
    return address[1]	

if __name__ == "__main__":
    f = sys.stdout

    k = int(input())

    from_cnt = 0
    from_cnt = int(input())
    from_i = 0
    frm = []
    while from_i < from_cnt:
        from_item = int(input())
        frm.append(from_item)
        from_i += 1


    to_cnt = 0
    to_cnt = int(input())
    to_i = 0
    to = []
    while to_i < to_cnt:
        to_item = int(input())
        to.append(to_item)
        to_i += 1

    root = build_tree(frm, to)

    res = find_height(root)
    f.write(str(res) + "\n")


    f.close()