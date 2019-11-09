#!/usr/bin/python
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

	def buildFromRawValues(self):
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
	inputBinaryTree.buildFromRawValues()
	return inputBinaryTree.root

def recursiveAdder(root):
	if root.left_ptr == None and root.right_ptr == None:
		return 1, root.val
	elif root.left_ptr != None and root.right_ptr == None:
		count, unival = recursiveAdder(root.left_ptr)
		if root.val == root.left_ptr.val and unival == root.val:
			return count+1, unival
		else:
			return count, None
	elif root.left_ptr == None and root.right_ptr != None:
		count, unival = recursiveAdder(root.right_ptr)
		if root.val == root.right_ptr.val and unival == root.val:
			return count+1, unival
		else:
			return count, None
	else:
		left_count, left_unival = recursiveAdder(root.left_ptr)
		right_count, right_unival = recursiveAdder(root.right_ptr)
		if root.val == root.right_ptr.val and root.val == root.left_ptr.val and left_unival == right_unival and right_unival == root.val:
			return left_count+right_count+1, left_unival
		else:
			return left_count+right_count, None

def findSingleValueTrees(root):
    if root:
    	final_count, unival = recursiveAdder(root)
    	return final_count
    return 0

def main():
	root = readBinaryTree()
	result = findSingleValueTrees(root)
	print(result)

main()
