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

    def insert(self, index, item):

        if index == 0:
            # inserting at the head
            old_head = self.head
            self.head = Node(item, old_head)
        elif index == self.length - 1:
            # inserting at end
            self.__append_helper__(item)
        else:
            # inserting into middle
            prev_node = self.get(index - 1)
            cur_node = prev_node.next_node
            prev_node.next_node = Node(item, cur_node)

        self.length += 1

    def last_node(self):
        return self.get(self.length - 1)

    def append(self, item):
        self.__append_helper__(item)
        self.length += 1

    def __append_helper__(self, item):
        new_node = Node(item, None)
        if self.head is None:
            # appending as the first item in the list
            self.head = new_node
        else:
            self.last_node().next_node = new_node


ll = LinkedList()
for i in range(0, 10):
    ll.append(i)
for i in range(0, ll.length):
    print(ll.get(i).item)
