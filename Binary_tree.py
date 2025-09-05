class Node:
    def __init__(self,value):
        self.value = None
        self.left=None
        self.right= None
class Binary_search:
    def __init__(self):
        self.root=None

    def insert(self,value):
        def insert(node,value):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = insert(node.left,value)
            elif value > node.value:
                node.right = _insert(node.right,value)
            return node
        
    def serach(self,value):
        def _search(node,value):
            if node is None:
                return False
            if value == node.value:
                return True
            elif value < node.value:
                return _search(node.left,value)
            else:
                return _seacrh(node.right,value)

        return _search(self.root,value)


    def inorder(self):
        result=[]
        def _inorder(node):
            if  node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
            _inorder(slef.root)               
            return result 
        
    def post_order(self):
        result=[]
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.value)
            _postorder(self.root)
            return result
        


bst= BInary_search()
for val in [50,30,70,20,40,60,80]:
    bst.insert(val)

print("inorder",bst.inorder())
print("preorder",bst.preorder)
print("postorder",bst.postorder())



