class Node(object):

    def __init__(self, num):
        self.num = num
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class Graph(object):

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.num] = node

    def dfs(self, start, target):
        start = self.nodes[start]
        target = self.nodes[target]
        visited = {}
        return self.dfs_helper(start, target, visited)

    def dfs_helper(self, start, target, visited):
        print(start.num)
        if start in visited:
            return False
        visited[start] = True
        if start is target:
            return True
        for child in start.children:
            if self.dfs_helper(child, target, visited):
                return True
        return False
