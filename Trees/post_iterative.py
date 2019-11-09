#!/usr/bin/env python
from isBST import TreeNode, BinaryTree, readBinaryTree

# Using one stack
def build_stack(node, s):
    while node:
        if node.right_ptr:
            s.append(node.right_ptr)
        s.append(node)
        node = node.left_ptr

def peek(s):
    if len(s) > 0:
        return s[-1]
    return None

def post_iterative_1_stack(root):
    s = []
    build_stack(root, s)

    while s:
        curr = s.pop()
        if curr.right_ptr == peek(s):
            temp = s.pop()
            s.append(curr)
            build_stack(temp, s)
        else:
            print(curr.val)

# Using two stacks

def dfs(node):

    if node is None:
        return

    print(node.val)
    dfs(node.left_ptr)
    dfs(node.right_ptr)

def post_iterative_2_stack(root):

    # dfs(root)
    s1 = []
    s2 = []

    s1.append(root)
    while s1:
        curr = s1.pop()
        s2.append(curr)
        if curr.right_ptr:
            s1.append(curr.right_ptr)
        if curr.left_ptr:
            s1.append(curr.left_ptr)

    while s2:
        curr = s2.pop()
        print(curr.val)

def main():

    root = readBinaryTree()
    post_iterative_2_stack(root)
    post_iterative_1_stack(root)

if __name__ == '__main__':
    main()
