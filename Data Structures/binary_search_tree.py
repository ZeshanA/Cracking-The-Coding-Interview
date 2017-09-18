class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value <= self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def print(self, order='in_order'):
        if order == 'pre_order':
            print(self.data)
        if self.left is not None:
            self.left.print(order)
        if order == 'in_order':
            print(self.data)
        if self.right is not None:
            self.right.print(order)
        if order == 'post_order':
            print(self.data)


a = Node(8)
a.insert(7)
a.insert(9)
a.print('in_order')
