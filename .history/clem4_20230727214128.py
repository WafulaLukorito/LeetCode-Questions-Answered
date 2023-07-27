def sumdepth(root):
    return sum_depths(root, 0)


def sum_depths(root, height):
    if not root:
        return 0
    
    left_depth = sum_depths(root.left, height+1)
    right_depth = sum_depths(root.right, height+1)
    
    total_depth = left_depth + right_depth + height
    
    return total_depth