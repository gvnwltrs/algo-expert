# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right
            
        return self

    def contains(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False

    def remove(self, value, parent_node = None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.get_min_value()
                self.right.remove(self.value, self)
            elif parent_node is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right 
                else:
                    pass
            elif parent_node.left == self:
                parent_node.left = self.left if self.left is not None else self.right
            elif parent_node.right == self:
                parent_node.right = self.left if self.left is not None else self.right
        return self

    def get_min_value(self):
        if self.left is None:
            return self.value
        else:
            return self.left.get_min_value()
