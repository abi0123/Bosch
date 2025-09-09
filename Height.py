def Binary_height(root):
   
    if root is None:
        return -1  

    left_height = Binary_height(root.left)
    right_height = Binary_height(root.right)
    return 1 + max(left_height, right_height)

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(Binary_height(root)) 


