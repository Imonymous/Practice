#!/usr/bin/env python3

import sys
from collections import deque
sys.setrecursionlimit(100000 + 1000)
class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

class BinaryTree():
    class Edge():
        def __init__(self, parentNodeIndex = None, childNodeIndex = None, leftRightFlag = None):
            self.BinaryTree = BinaryTree
            self.parentNodeIndex = parentNodeIndex
            self.childNodeIndex = childNodeIndex
            self.leftRightFlag = leftRightFlag

    def __init__(self):
        self.root = None;
        self.noOfNodes = 0
        self.noOfEdges = 0
        self.rootIndex = -1
        self.nodeValues=[]
        self.edges=[]

    def readRawValues(self):
        self.noOfNodes = int(input())
        if self.noOfNodes > 0:
            nodeValueString = input().split(' ')
            for val in nodeValueString:
                self.nodeValues.append(int(val))

        self.rootIndex = int(input())
        self.noOfEdges = int(input())
        for i in range(self.noOfEdges):
            edgeInput = input().split(' ')
            self.edges.append(self.Edge(int(edgeInput[0]), int(edgeInput[1]), edgeInput[2]))

    def buildFormRawValues(self):
        if self.noOfNodes == 0:
            root =  None
            return
        nodes = []
        for i in range(self.noOfNodes):
            nodes.append(TreeNode(self.nodeValues[i]))

        for i in range(self.noOfEdges):
            if self.edges[i].leftRightFlag == "L":
                nodes[self.edges[i].parentNodeIndex].left_ptr = nodes[self.edges[i].childNodeIndex]
            else:
                nodes[self.edges[i].parentNodeIndex].right_ptr = nodes[self.edges[i].childNodeIndex]

        self.root = nodes[self.rootIndex]

def readBinaryTree():
    inputBinaryTree = BinaryTree()
    inputBinaryTree.readRawValues()
    inputBinaryTree.buildFormRawValues()
    return inputBinaryTree.root

def printCircularList(circularListHead):
    if circularListHead == None:
        print()
        return;
    tmpHead = circularListHead;
    while tmpHead.right_ptr != circularListHead:
        print(tmpHead.val, end= ' ')
        tmpHead = tmpHead.right_ptr
    print(tmpHead.val)

# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

# Attempt 1
# def inOrder(node, inorderarr):
#     if node is None:
#         return
#
#     inOrder(node.left_ptr, inorderarr)
#     inorderarr.append(node)
#     inOrder(node.right_ptr, inorderarr)
#
# def BTtoLL(root):
#     if not root:
#         return
#     inorderarr = []
#     inOrder(root, inorderarr)
#     for i in range(1, len(inorderarr)):
#         inorderarr[i].left_ptr = inorderarr[i-1]
#         inorderarr[i-1].right_ptr = inorderarr[i]
#
#     inorderarr[len(inorderarr)-1].right_ptr = inorderarr[0]
#     inorderarr[0].left_ptr = inorderarr[len(inorderarr)-1]
#
#     return inorderarr[0]


# Attempt 2 - Not working due to head and tail being immutable references
import copy
def inOrder(node, head, tail):
    if node is None:
        return

    inOrder(node.left_ptr, head, tail)
    if head.val is None:
        print("Aha")
        head = copy.deepcopy(node)

    if tail.val is None:
        tail = copy.deepcopy(node)
    else:
        tail.right_ptr = node
        node.left_ptr = tail

    tail = copy.deepcopy(node)

    inOrder(node.right_ptr, head, tail)

def BTtoLL(root):
    if not root:
        return
    head = TreeNode()
    tail = TreeNode()
    inOrder(root, head, tail)
    head.left_ptr = tail
    tail.right_ptr = head

    return head

def main():
    root = readBinaryTree()
    result = BTtoLL(root)
    printCircularList(result)

main()
