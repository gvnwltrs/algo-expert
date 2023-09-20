# This is an input class. Do not edit.
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
