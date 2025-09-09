class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.key, end=" ")  
        preorder(root.left)    
        preorder(root.right)   


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Preorder traversal:")
    preorder(root)
