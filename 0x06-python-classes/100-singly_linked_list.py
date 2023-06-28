#!/usr/bin/python3
""""This module contains a class represention for node & singly linked list."""


class Node:
    """This class represents a node."""
    def __init__(self, data, next_node=None):
        """
        This functin initalizes the node.

        Args:
            data (int): The data.
            next_node (Node): The next node. Defaults to None.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """This function gets the private instance attribute: data."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        This function sets the private instance attribute: data.

        Args:
            value (int): The new value of data.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This function gets the private instance attribute: next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        This function sets the private instance attribute: data.

        Args:
            value (Node): The new value of next_node.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly linked list."""
    def __init__(self):
        """This functin initalizes the singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """
        This function inserts a new Node
        into the correct sorted position in the list

        Args:
            value (int): the new data.
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """
        This functin returns a the human-readable
        representation of a singly linked list.
        """
        str = ""
        temp_node = self.__head
        while temp_node is not None:
            str += "{}".format(temp_node.data)
            if temp_node.next_node is not None:
                str += "\n"
            temp_node = temp_node.next_node
        return str
