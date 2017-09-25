class MinHeap(object):
    
    def __init__(self):
        self._items = []

    def get_left_child_index(self, parent):
        return (2 * parent) + 1

    def get_right_child_index(self, parent):
        return (2 * parent) + 2

    def get_parent_index(self, child):
        return int((child - 1) / 2)

    def get_left_child(self, parent):
        return self._items[self.get_left_child_index(parent)]

    def get_right_child(self, parent):
        return self._items[self.get_right_child_index(parent)]

    def get_parent(self, child):
        return self._items[self.get_parent_index(child)]

    def has_left_child(self, parent):
        return self.get_left_child_index(parent) < len(self._items)

    def has_right_child(self, parent):
        return self.get_right_child_index(parent) < len(self._items)

    def has_parent(self, child):
        return self.get_parent_index(child) >= 0

    def swap_items(self, i1, i2):
        temp = self._items[i1]
        self._items[i1] = self._items[i2]
        self._items[i2] = temp

    def peek(self):
        if len(self._items) == 0:
            raise IndexError()
        return self._items[0]

    def remove_min(self):
        minimum = self._items[0]
        last_item_index = len(self._items) - 1
        self._items[0] = self._items[last_item_index]
        del self._items[last_item_index]
        self.heapify_down()
        return minimum

    def add(self, item):
        self._items.append(item)
        self.heapify_up()

    def heapify_up(self):
        index = len(self._items) - 1
        while self.has_parent(index) and self.get_parent(index) > self._items[index]:
            self.swap_items(index, self.get_parent_index(index))
            index = self.get_parent(index)

    def heapify_down(self):
        index = 0

        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.get_right_child(index) > self.get_left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self._items[index] < self._items[smaller_child_index]:
                break
            else:
                self.swap_items(index, self.get_left_child_index(index))

            index = smaller_child_index

    def print(self):
        print(self._items)
