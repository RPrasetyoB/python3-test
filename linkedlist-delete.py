# Linked List Delete Operation
# You are tasked with implementing a basic linked list data structure in Python. Your linked list should support the following operations:
# insert(val: int): Insert a new node with the given integer value at the end of the linked list.
# delete(val: int): Delete the same node with the given integer value from the linked list, if it exists.
# display() -> String: Return a list of string in the linked list in the order they appear.
# Example:
# Input
# list=[10, 20, 30, 40, 50]
# Function
# delete=30
# Output
# 10 -> 20 -> 40 -> 50 -> None

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, val):
        if not self.head:
            return

        if self.head.data == val:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == val:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        if not self.head:
            return "Empty List"
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"

if __name__ == "__main":
    linked_list = LinkedList()
    print("Initial Linked List:")
    print(linked_list.display())

    values = [10, 20, 30, 40, 50]
    for value in values:
        linked_list.insert(value)
    print("Updated Linked List:")
    print(linked_list.display())

    delete_value = 30
    linked_list.delete(delete_value)
    print(f"Linked List after deleting {delete_value}:")
    print(linked_list.display())


# do not modify this function call
retcode = pytest.main(['-v'])