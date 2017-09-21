class Node(object):
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.isWord = False

    def insert(self, string):
        if len(string) == 0:
            self.isWord = True
            return

        if string[0] == self.char:
            if self.children.get(string[1]) is None:
                self.children[string[1]] = Node(string[1])
            self.children[string[1]].insert(string[2:])
        else:
            # First char is not one of this node's children
            if self.children.get(string[0]) is None:
                # Add a new child node, containing first char of the string
                self.children[string[0]] = Node(string[0])

            # Insert rest of the string into child node containing first char
            self.children[string[0]].insert(string[1:])

    def contains(self, word):
        if len(word) == 0:
            return self.isWord
        elif len(word) == 1:
            return self.char == word

        if self.char != word[0]:
            return False
        elif word[1] not in self.children:
            return False
        else:
            return self.children.get(word[1]).contains(word[1:])


a = Node('c')
a.insert('careful')
a.insert('car')
print(a)
print(a.contains('card'))
print(a.contains('careful'))
