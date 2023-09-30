# We are given an acyclic tree-like graph. Each node in this graph is going to be an instance of a Node class, and is going to have a name and optionally some children nodes. We are asked to write a depthFirstSearch method on the Node class, which is going to accept an empty array as argument and perform a depth-first search on the graph. As we traverse the graph, we need to store the names of all the nodes in the input array and return that array. The nodes should be visited from left to right.


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            print('now in: {0}'.format(child.name))
            child.depthFirstSearch(array)
        return array