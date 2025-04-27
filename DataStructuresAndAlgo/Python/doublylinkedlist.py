class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def append_at_start(self, data):
        """appends data to the start of the linked list: O(1)!!"""
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.__size += 1

    def size(self):
        """the size of the list """
        return self.__size

    def append(self, data):
        """appends data to the end of the linked list: O(1)!!"""
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
        self.__size += 1

    def inser(self, data):
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

    def __str__(self):
        """returns the string representation of the list"""
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return " <-> ".join(result)
