class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        node_end = Node(data)
        if self.head is None:  
            self.head = node_end
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node_end

    def insert_position(self, position, data):
        np = Node(data)
        temp = self.head
        for i in range(position - 1): 
            temp = temp.next
        np.data=data   
        np.next = temp.next
  
    def display(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" --> ")
                temp = temp.next
            print("None")

L = SingleLinkedList()

n = Node(10)
L.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
L.insert_beginning(4) 
L.insert_end(50)  
L.insert_position(2, 15)

L.display()
