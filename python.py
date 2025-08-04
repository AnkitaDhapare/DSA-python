#singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # is head empty
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Example
sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.display()
