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

    def set(self, index, item):
        node = self.get(index)
        node.item = item

    def delete(self, index):
        if index == 0:
            # index is head of list
            self.head = self.head.next_node
        elif index == self.length - 1:
            # index is last in list
            penultimate_node = self.get(self.length - 2)
            penultimate_node.next_node = None
        else:
            # index is in middle of list
            prev_node = self.get(index - 1)
            cur_node = prev_node.next_node
            post_node = cur_node.next_node

            prev_node.next_node = post_node
            
        self.length -= 1
