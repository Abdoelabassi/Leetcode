"""Singly linked list:"""


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def size(self):
        """the size of the list"""
        return self.__size

    def append(self, data):
        """appends data to the linked list: O(1)!!"""
        node = Node(data)
        if self.tail:
            self.__size += 1
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def insert(self, data):
        """insert a new node at certain index"""
        current = self.head
        prev = self.head
        node = Node(data)
        while current:
            if current.data == data:
                self.__size += 1
                node.next = current
                prev.next = node
            prev = current
            current = current.next

    def delete_first(self):
        """deletes the fist node"""
        current = self.head
        if self.head is None:
            print("No data elment to delete")
        elif current == self.head:
            self.__size -= 1
            self.head = current.next

    def delete_last(self):
        """deletes the last node"""
        current = self.head
        prev = self.head
        while current:
            if current.next is None:
                prev.next = current.next
                self.__size -= 1
            prev = current
            current = current.next

    def delete(self, data):
        """deletes a node at any position"""
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.__size -= 1
                return
            prev = current
            current = current.next

    def clear(self):
        """clear a list"""
        self.tail = None
        self.head = None

    def search(self, data) -> bool:
        """search an item in the list"""
        for value in self.iter():
            if value == data:
                return True
        return False

    def iter(self):
        current: Node = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def __str__(self):
        """string representation"""
        return f"{self.__class__.__name__}()"


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
