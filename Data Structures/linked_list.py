class Node(object):
    def __init__(self, item, next_node):
        self.item = item
        self.next_node = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index):
        if index == 0:
            return self.head
        else:
            cur_node = self.head
            for i in range(0, index):
                cur_node = cur_node.next_node
            return cur_node
