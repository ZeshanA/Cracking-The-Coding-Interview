class Queue(object):

    def __init__(self):
        self.__list__ = []
        self.length = 0

    def append(self, item):
        self.__list__.append(item)
        self.length += 1

    def pop(self):
        head = self.__list__[0]
        self.__list__.remove(head)
        return head

    def __str__(self):
        return self.__list__.__str__()
