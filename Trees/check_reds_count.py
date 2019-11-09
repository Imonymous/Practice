# Binary tree, 2 colors - red or blue, path = root to leaf
# bool func to check all paths have same number of red nodes

'''

   R
 R   B
B B R R

'''

def helper(node, reds_so_far, reds_per_path):

    if node is None:
        if not reds_per_path:
            reds_per_path.append(reds_so_far)
            return True
        else:
            if reds_per_path[0] == reds_so_far:
                return True
            else:
                return False

    if node.color == "Red":
        return helper(node.left, reds_so_far+1, reds_so_far) and helper(node.right, reds_so_far+1, reds_per_path)
    else:
        return helper(node.left, reds_so_far, reds_so_far) and helper(node.right, reds_so_far, reds_per_path)

def check_red_count(root):

    return helper(root, 0, [])
