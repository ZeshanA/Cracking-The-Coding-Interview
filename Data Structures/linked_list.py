class Node(object):
    def __init__(self, item, next_node):
        self.item = item
        self.next_node = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0
