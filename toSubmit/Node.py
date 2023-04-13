from typing import List

"""
Unordered Tree Node
----------
This class represents an individual Node in an unordered Tree. 
Each Node consists of the following properties:
    - id: The id of the Node
    - children: A list of the children for the Node
    - parent: The parent of the Node
The class also supports the following functions:
    - add_child(Node): Adds the given Node as a child of the current Node (MUST RUN IN O(1) TIME)
    - get_children(): Returns the children of the current Node
    - get_parent(): Returns the parent of the current Node
    - set_parent(Node): Sets the parent of the current Node
Your task is to complete the following functions which are marked by the TODO comment.
You are free to add properties and functions to the class as long as the given signatures remain identical
"""


class Node:
    # These are the defined properties as described above, feel free to add more if you wish!
    id: int
    children: List["Node"]
    parent: "Node"

    def __init__(self, id: int) -> None:
        """
        The constructor for the Node class.
        :param id: The id of the node.
        """

        # TODO: Add your code here!

    def add_child(self, u: "Node") -> None:
        """
        Adds the given node as a child of the current node.
        The given node is guaranteed to not be a child of any other node.
        This should run in O(1) time.
        :param node: The node to add as a child.
        """

        # TODO: Add your code here!

    def get_children(self) -> List["Node"]:
        """
        Returns the children of the current node.
        :return: The children of the current node.
        """

        # TODO: Add your code here!

    def get_parent(self) -> "Node":
        """
        Returns the parent of the current node.
        :return: The parent of the current node.
        """

        # TODO: Add your code here!

    def set_parent(self, u: "Node") -> None:
        """
        Sets the parent of the current node.
        :param u: The parent node.
        """

        # TODO: Add your code here!

