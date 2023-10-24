#!/usr/bin/python3
"""
Singly Linked List Node and Singly Linked List class implementation
"""

class Node:
    """
    Node class defines a node of a singly linked list.

    Attributes:
        data (int): The data to store in the node.
        next_node (Node): The next node in the list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the list.
        
        Raises:
            TypeError: If data is not an integer or next_node is not a Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data from the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data in the node.

        Args:
            value (int): The data to store in the node.
        
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the list.

        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the list.

        Args:
            value (Node): The next node in the list.
        
        Raises:
            TypeError: If value is not a Node or None.
        """
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    SinglyLinkedList class defines a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance with an empty list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The data to insert in the list.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string containing the elements of the linked list.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
