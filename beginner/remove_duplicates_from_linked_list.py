# This is an input class. Do not edit.


# We are given the head of a singly linked list. The nodes of the linked list are going to be sorted in ascending order with respect to their values and the values are going to be integers. We are asked to write a function that is going to remove all the nodes with duplicate values and return the modified linked list. The linked list should be modified in place and the nodes should remain in their original order.



class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    cur_node = linkedList
    while cur_node is not None:
        next_node = cur_node.next
        while next_node is not None and next_node.value == cur_node.value:
            next_node = next_node.next

        cur_node.next = next_node
        cur_node = next_node

    return linkedList
