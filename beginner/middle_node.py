# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    middle_node = None
    
    count = 0
    cur_node = linkedList
    while cur_node is not None:
        count += 1
        cur_node = cur_node.next
    print('count is: {0}'.format(count))
    select = count // 2

    if count == 1:
        return linkedList

    count = 0 
    cur_node = linkedList
    while count < select:
        count += 1
        cur_node = cur_node.next

    middle_node = cur_node
    
    return middle_node
