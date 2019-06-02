#!/usr/bin/env python

import sys
from collections import deque

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

def preOrder(root, so_far):
    if root is None:
        return
    elif root.left_ptr is None and root.right_ptr is None:
        so_far.append(root.val)
        print(" ".join(str(x) for x in so_far))
        so_far.pop()
        return

    so_far.append(root.val)
    preOrder(root.left_ptr, so_far)
    preOrder(root.right_ptr, so_far)

    if len(so_far) > 0:
        so_far.pop()
    return

def printAllPaths(root):
    preOrder(root, [])
    return

def main():
    root = readBinaryTree()
    printAllPaths(root)

main()