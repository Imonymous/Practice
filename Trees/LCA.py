#!/usr/bin/env python3

# Mock 6

import sys

sys.setrecursionlimit(101000)

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    if node == None:
        return None
    preorder(node.left)
    preorder(node.right)

#class Node(object):
#    def __init__(self, data, left=None, right=None):
#        self.data = data
#        self.left = left
#        self.right = right

def prepareForRMQ(node, euler, levels, first_occ, current_level):
    if not node:
        return

    euler.append(node.data)
    levels.append(current_level)
    if node.left:
        if node.left.data not in first_occ.keys():
            first_occ[node.left.data] = len(levels)
        prepareForRMQ(node.left, euler, levels, first_occ, current_level+1)
        euler.append(node.data)
        levels.append(current_level)
    if node.right:
        if node.right.data not in first_occ.keys():
            first_occ[node.right.data] = len(levels)
        prepareForRMQ(node.right, euler, levels, first_occ, current_level+1)
        euler.append(node.data)
        levels.append(current_level)

def RMQ(euler, levels, first_occ, a, b):

    lo = min(a.data, b.data)
    hi = max(a.data, b.data)
    idx_a = first_occ[a.data]
    idx_b = first_occ[b.data]

    idx_lo = min(idx_a, idx_b)
    idx_hi = max(idx_a, idx_b)

    sublist = levels[idx_lo:idx_hi+1]

    mini = min(sublist)

    min_idx = idx_lo + sublist.index(mini)

    return euler[min_idx]

def lca(root, a, b):
    #Write your code here
    euler = []
    levels = []
    first_occ = dict()
    first_occ[root.data] = 0
    prepareForRMQ(root, euler, levels, first_occ, 1)

    res = RMQ(euler, levels, first_occ, a, b)

    return res

numbers = [int(n) for n in input().split()]
n=numbers[0]
a=numbers[1]
b=numbers[2]

i=0
xx=[]
while i<=n:
    xx.insert(i,Node(i,None,None))
    i+=1;
i=1
while i<n:
    num = [int(n) for n in input().split()]
    st=num[0]
    en=num[1]
    if xx[st].left==None:
        xx[st].left=xx[en]
    else:
        xx[st].right=xx[en]
    i+=1

print(lca(xx[1], xx[a], xx[b]))
