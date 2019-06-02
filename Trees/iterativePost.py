#!/usr/bin/env python
import sys
from collections import deque

sys.setrecursionlimit(101000)

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

def postorderTraversal(root):
	s = []
	ans = []
	p = root
	while len(s) > 0 or p != None:
		if p != None:
			s.append(p)
			p = p.left_ptr
		else:
			temp = s[-1].right_ptr

			if temp == None:
				temp = s.pop()
				ans.append(temp.val)

				while len(s) > 0 and temp == s[-1].right_ptr:
					temp = s.pop()
					ans.append(temp.val)
			
			else:
				p = temp

	print(" ".join(str(x) for x in ans))

def main():
    root = readBinaryTree()
    postorderTraversal(root)

main()