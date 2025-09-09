class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = SinglyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        print()

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.insert(40)

    print("Elements of Linked List:")
    ll.printLinkedList()



